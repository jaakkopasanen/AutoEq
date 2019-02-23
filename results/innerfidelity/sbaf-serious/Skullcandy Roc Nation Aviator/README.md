# Skullcandy Roc Nation Aviator
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.9; 45 -2.9; 49 -3.7; 54 -4.5; 60 -5.4; 66 -6.1; 72 -6.7; 79 -7.3; 87 -7.9; 96 -8.5; 106 -8.7; 116 -8.8; 128 -9.1; 141 -9.2; 155 -9.3; 170 -9.2; 187 -9.1; 206 -9.1; 227 -8.7; 249 -8.6; 274 -8.3; 302 -8.0; 332 -7.7; 365 -7.4; 402 -7.2; 442 -6.8; 486 -6.6; 535 -6.0; 588 -5.3; 647 -5.2; 712 -4.4; 783 -2.7; 861 -2.4; 947 -2.2; 1042 -2.9; 1146 -3.1; 1261 -3.7; 1387 -5.6; 1526 -6.7; 1678 -7.1; 1846 -7.1; 2031 -6.6; 2234 -5.9; 2457 -5.0; 2703 -5.0; 2973 -5.9; 3270 -6.7; 3597 -6.3; 3957 -7.6; 4353 -11.3; 4788 -10.8; 5267 -6.7; 5793 -3.1; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -9.5; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Roc Nation Aviator GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Roc Nation Aviator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.57 | 7.5 dB  |
| Peaking | 110 Hz  | 0.43 | -4.0 dB |
| Peaking | 912 Hz  | 1.72 | 4.8 dB  |
| Peaking | 4563 Hz | 5.39 | -6.3 dB |
| Peaking | 6173 Hz | 4.84 | 5.5 dB  |
| Peaking | 1226 Hz | 6.49 | 1.7 dB  |
| Peaking | 1679 Hz | 2.16 | -1.6 dB |
| Peaking | 2538 Hz | 4.02 | 2.0 dB  |
| Peaking | 8828 Hz | 1.35 | 1.3 dB  |
| Peaking | 9456 Hz | 3.44 | -4.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Roc%20Nation%20Aviator/Skullcandy%20Roc%20Nation%20Aviator.png)