# Skullcandy Holua
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.5; 23 -14.5; 25 -14.4; 28 -14.4; 31 -14.3; 34 -14.2; 37 -14.2; 41 -14.1; 45 -14.1; 49 -14.0; 54 -14.0; 60 -13.9; 66 -13.9; 72 -13.9; 79 -13.8; 87 -13.8; 96 -13.6; 106 -13.3; 116 -13.1; 128 -12.9; 141 -12.6; 155 -12.3; 170 -11.9; 187 -11.5; 206 -11.0; 227 -10.4; 249 -9.9; 274 -9.3; 302 -8.7; 332 -8.0; 365 -7.3; 402 -6.6; 442 -6.3; 486 -5.8; 535 -5.3; 588 -4.7; 647 -4.3; 712 -3.9; 783 -3.8; 861 -3.9; 947 -4.3; 1042 -4.9; 1146 -5.2; 1261 -5.6; 1387 -6.6; 1526 -8.4; 1678 -9.9; 1846 -11.2; 2031 -12.5; 2234 -13.9; 2457 -13.3; 2703 -8.2; 2973 -3.8; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -2.4; 4788 -5.1; 5267 -6.3; 5793 -2.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Holua GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.16 | -7.6 dB  |
| Peaking | 195 Hz  | 0.44 | -4.3 dB  |
| Peaking | 1359 Hz | 0.25 | 6.2 dB   |
| Peaking | 2306 Hz | 1.2  | -17.1 dB |
| Peaking | 3308 Hz | 1.74 | 10.5 dB  |
| Peaking | 1636 Hz | 8.62 | -0.8 dB  |
| Peaking | 4130 Hz | 7.6  | 1.8 dB   |
| Peaking | 5210 Hz | 3.93 | -4.0 dB  |
| Peaking | 6187 Hz | 3.47 | 6.8 dB   |
| Peaking | 7632 Hz | 1.42 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)