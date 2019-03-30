# Monster Diesel Vektr
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.5; 28 -7.0; 31 -7.3; 34 -7.6; 37 -7.9; 41 -8.1; 45 -8.1; 49 -7.9; 54 -7.9; 60 -8.3; 66 -9.0; 72 -9.8; 79 -10.5; 87 -11.0; 96 -11.4; 106 -11.7; 116 -11.7; 128 -11.6; 141 -11.0; 155 -10.1; 170 -9.1; 187 -8.3; 206 -7.5; 227 -7.0; 249 -6.8; 274 -6.8; 302 -6.7; 332 -6.3; 365 -5.6; 402 -4.6; 442 -3.6; 486 -3.2; 535 -3.4; 588 -3.8; 647 -4.1; 712 -4.2; 783 -4.2; 861 -4.1; 947 -3.6; 1042 -2.9; 1146 -2.3; 1261 -1.7; 1387 -1.0; 1526 -0.5; 1678 -0.5; 1846 -0.8; 2031 -1.2; 2234 -1.6; 2457 -1.5; 2703 -1.3; 2973 -1.7; 3270 -2.5; 3597 -3.7; 3957 -4.7; 4353 -6.1; 4788 -8.4; 5267 -9.4; 5793 -8.3; 6373 -6.7; 7010 -6.8; 7711 -7.3; 8482 -6.4; 9330 -5.2; 10263 -5.2; 11289 -5.5; 12418 -5.6; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Diesel Vektr GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Diesel Vektr ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 1.36 | -1.7 dB |
| Peaking | 111 Hz  | 0.95 | -6.7 dB |
| Peaking | 1922 Hz | 0.57 | 4.5 dB  |
| Peaking | 3947 Hz | 1.35 | 2.5 dB  |
| Peaking | 5010 Hz | 1.48 | -6.9 dB |
| Peaking | 321 Hz  | 3.54 | -1.0 dB |
| Peaking | 480 Hz  | 2.53 | 2.0 dB  |
| Peaking | 831 Hz  | 1.87 | -1.1 dB |
| Peaking | 1494 Hz | 4.68 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Diesel%20Vektr/Monster%20Diesel%20Vektr.png)