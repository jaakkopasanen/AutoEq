# Skullcandy Holua
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.3; 23 -15.2; 25 -15.1; 28 -15.0; 31 -14.8; 34 -14.7; 37 -14.6; 41 -14.4; 45 -14.3; 49 -14.2; 54 -14.0; 60 -13.9; 66 -13.8; 72 -13.7; 79 -13.6; 87 -13.5; 96 -13.4; 106 -13.2; 116 -12.9; 128 -12.7; 141 -12.4; 155 -12.1; 170 -11.6; 187 -11.2; 206 -10.7; 227 -10.2; 249 -9.7; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.5; 402 -7.0; 442 -6.4; 486 -6.0; 535 -5.6; 588 -4.9; 647 -4.7; 712 -4.6; 783 -4.3; 861 -4.6; 947 -4.9; 1042 -5.6; 1146 -6.1; 1261 -6.7; 1387 -7.6; 1526 -8.8; 1678 -9.9; 1846 -10.9; 2031 -11.9; 2234 -13.7; 2457 -13.7; 2703 -10.2; 2973 -6.4; 3270 -3.1; 3597 -1.9; 3957 -4.3; 4353 -8.6; 4788 -15.4; 5267 -10.7; 5793 -4.3; 6373 -0.5; 7010 -2.8; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Holua GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Holua ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.2  | -9.6 dB  |
| Peaking | 154 Hz  | 0.82 | -3.5 dB  |
| Peaking | 2342 Hz | 1.67 | -15.0 dB |
| Peaking | 3598 Hz | 0.81 | 10.0 dB  |
| Peaking | 4804 Hz | 4.79 | -16.7 dB |
| Peaking | 757 Hz  | 1.9  | 1.8 dB   |
| Peaking | 1580 Hz | 4.23 | -1.5 dB  |
| Peaking | 5325 Hz | 9.15 | -1.9 dB  |
| Peaking | 6468 Hz | 4.5  | 5.2 dB   |
| Peaking | 7903 Hz | 1.45 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.0 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Holua/Skullcandy%20Holua.png)