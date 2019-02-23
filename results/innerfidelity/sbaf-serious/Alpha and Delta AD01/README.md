# Alpha and Delta AD01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.5; 25 -13.5; 28 -13.6; 31 -13.5; 34 -13.5; 37 -13.4; 41 -13.3; 45 -13.2; 49 -13.1; 54 -13.0; 60 -13.0; 66 -12.9; 72 -12.8; 79 -12.8; 87 -12.8; 96 -12.8; 106 -12.5; 116 -12.3; 128 -12.1; 141 -11.9; 155 -11.6; 170 -11.2; 187 -10.8; 206 -10.4; 227 -10.0; 249 -9.6; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.6; 402 -7.2; 442 -6.6; 486 -6.3; 535 -5.9; 588 -5.2; 647 -4.9; 712 -4.8; 783 -4.5; 861 -4.8; 947 -5.2; 1042 -5.6; 1146 -5.9; 1261 -6.4; 1387 -7.0; 1526 -7.8; 1678 -8.7; 1846 -9.2; 2031 -9.7; 2234 -9.9; 2457 -9.0; 2703 -7.3; 2973 -4.3; 3270 -1.1; 3597 -0.5; 3957 -2.3; 4353 -5.8; 4788 -6.6; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Alpha and Delta AD01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha and Delta AD01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.1  | -6.9 dB |
| Peaking | 898 Hz   | 0.57 | 4.6 dB  |
| Peaking | 2649 Hz  | 0.55 | -7.5 dB |
| Peaking | 3428 Hz  | 2.53 | 12.1 dB |
| Peaking | 5976 Hz  | 2.97 | 8.6 dB  |
| Peaking | 9328 Hz  | 2.36 | -0.6 dB |
| Peaking | 10693 Hz | 1.52 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20and%20Delta%20AD01/Alpha%20and%20Delta%20AD01.png)