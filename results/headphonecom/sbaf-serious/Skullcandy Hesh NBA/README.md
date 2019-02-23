# Skullcandy Hesh NBA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.7; 66 -3.5; 72 -4.6; 79 -6.5; 87 -8.1; 96 -9.2; 106 -9.7; 116 -9.8; 128 -9.9; 141 -10.1; 155 -9.9; 170 -9.9; 187 -10.0; 206 -10.1; 227 -9.8; 249 -9.6; 274 -9.4; 302 -9.1; 332 -9.2; 365 -9.2; 402 -9.3; 442 -9.6; 486 -9.8; 535 -10.1; 588 -10.4; 647 -10.4; 712 -9.8; 783 -9.0; 861 -9.2; 947 -8.9; 1042 -10.4; 1146 -12.7; 1261 -14.8; 1387 -14.3; 1526 -14.9; 1678 -12.2; 1846 -9.3; 2031 -6.3; 2234 -3.3; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.9; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh NBA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh NBA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 53 Hz   | 0.41 | 10.3 dB  |
| Peaking | 101 Hz  | 0.86 | -7.5 dB  |
| Peaking | 239 Hz  | 0.25 | -3.8 dB  |
| Peaking | 1471 Hz | 1.77 | -11.4 dB |
| Peaking | 3058 Hz | 0.73 | 8.6 dB   |
| Peaking | 2455 Hz | 5.41 | 2.4 dB   |
| Peaking | 3176 Hz | 1.2  | -1.3 dB  |
| Peaking | 4965 Hz | 3.12 | 1.6 dB   |
| Peaking | 5942 Hz | 5.61 | 2.5 dB   |
| Peaking | 9226 Hz | 2.7  | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -5.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Skullcandy%20Hesh%20NBA/Skullcandy%20Hesh%20NBA.png)