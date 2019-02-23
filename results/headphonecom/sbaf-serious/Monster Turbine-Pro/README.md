# Monster Turbine-Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.8; 23 -13.8; 25 -13.8; 28 -13.8; 31 -13.8; 34 -13.9; 37 -14.0; 41 -14.0; 45 -14.0; 49 -14.1; 54 -14.2; 60 -14.4; 66 -14.5; 72 -14.7; 79 -14.7; 87 -14.8; 96 -14.8; 106 -14.7; 116 -14.6; 128 -14.5; 141 -14.3; 155 -14.2; 170 -14.1; 187 -13.7; 206 -13.1; 227 -12.6; 249 -12.1; 274 -11.5; 302 -10.8; 332 -10.1; 365 -9.3; 402 -8.6; 442 -7.9; 486 -7.2; 535 -6.5; 588 -5.8; 647 -5.1; 712 -4.5; 783 -4.1; 861 -4.0; 947 -4.1; 1042 -4.4; 1146 -4.6; 1261 -5.0; 1387 -5.8; 1526 -6.6; 1678 -7.6; 1846 -8.4; 2031 -8.4; 2234 -7.9; 2457 -7.0; 2703 -5.6; 2973 -4.0; 3270 -2.4; 3597 -2.0; 3957 -3.3; 4353 -4.5; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Turbine-Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Turbine-Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.34 | -7.1 dB |
| Peaking | 113 Hz  | 0.88 | -4.8 dB |
| Peaking | 221 Hz  | 1.49 | -3.9 dB |
| Peaking | 3463 Hz | 4.43 | 4.4 dB  |
| Peaking | 5728 Hz | 2.97 | 6.6 dB  |
| Peaking | 228 Hz  | 4.12 | 1.1 dB  |
| Peaking | 373 Hz  | 0.78 | -3.1 dB |
| Peaking | 856 Hz  | 0.43 | 4.1 dB  |
| Peaking | 1895 Hz | 1.63 | -4.7 dB |
| Peaking | 8240 Hz | 3.99 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Turbine-Pro/Monster%20Turbine-Pro.png)