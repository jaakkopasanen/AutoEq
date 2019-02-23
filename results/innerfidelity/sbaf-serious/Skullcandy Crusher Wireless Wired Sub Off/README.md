# Skullcandy Crusher Wireless Wired Sub Off
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.5; 28 -9.0; 31 -9.4; 34 -9.7; 37 -10.1; 41 -10.3; 45 -10.3; 49 -10.3; 54 -11.0; 60 -10.8; 66 -9.5; 72 -8.1; 79 -8.7; 87 -11.1; 96 -12.1; 106 -11.8; 116 -12.2; 128 -13.4; 141 -13.7; 155 -12.7; 170 -12.3; 187 -12.1; 206 -11.0; 227 -9.6; 249 -8.3; 274 -7.0; 302 -5.7; 332 -4.9; 365 -3.7; 402 -2.9; 442 -2.1; 486 -1.7; 535 -1.3; 588 -0.5; 647 -1.4; 712 -2.6; 783 -3.1; 861 -3.0; 947 -2.8; 1042 -2.8; 1146 -2.7; 1261 -2.4; 1387 -2.8; 1526 -3.5; 1678 -4.1; 1846 -4.6; 2031 -4.9; 2234 -5.7; 2457 -5.9; 2703 -6.7; 2973 -7.5; 3270 -7.5; 3597 -6.9; 3957 -6.4; 4353 -7.1; 4788 -5.6; 5267 -3.6; 5793 -6.5; 6373 -6.4; 7010 -6.9; 7711 -8.4; 8482 -10.4; 9330 -11.6; 10263 -11.3; 11289 -9.7; 12418 -7.6; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Crusher Wireless Wired Sub Off GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Crusher Wireless Wired Sub Off ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 1.09 | -3.5 dB |
| Peaking | 148 Hz   | 0.92 | -7.5 dB |
| Peaking | 513 Hz   | 0.94 | 5.9 dB  |
| Peaking | 1294 Hz  | 2.01 | 2.8 dB  |
| Peaking | 9711 Hz  | 2.39 | -6.0 dB |
| Peaking | 74 Hz    | 5.1  | 4.5 dB  |
| Peaking | 76 Hz    | 2.22 | -2.3 dB |
| Peaking | 3115 Hz  | 3.94 | -1.7 dB |
| Peaking | 5215 Hz  | 8.68 | 3.3 dB  |
| Peaking | 20595 Hz | 3.1  | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 5.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Crusher%20Wireless%20Wired%20Sub%20Off/Skullcandy%20Crusher%20Wireless%20Wired%20Sub%20Off.png)