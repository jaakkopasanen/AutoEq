# Monster Elements Wireless Over-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.8; 25 -11.9; 28 -12.1; 31 -12.2; 34 -12.3; 37 -12.4; 41 -12.5; 45 -12.6; 49 -12.5; 54 -12.4; 60 -12.2; 66 -12.1; 72 -12.0; 79 -11.8; 87 -11.6; 96 -11.6; 106 -11.6; 116 -11.5; 128 -11.6; 141 -11.6; 155 -11.6; 170 -11.4; 187 -10.9; 206 -10.2; 227 -8.9; 249 -7.6; 274 -6.2; 302 -4.7; 332 -3.1; 365 -1.4; 402 -0.8; 442 -1.3; 486 -1.8; 535 -1.8; 588 -1.8; 647 -1.7; 712 -1.4; 783 -1.0; 861 -0.7; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -1.1; 1678 -2.0; 1846 -3.8; 2031 -6.1; 2234 -7.9; 2457 -9.0; 2703 -9.8; 2973 -10.1; 3270 -9.8; 3597 -9.7; 3957 -10.1; 4353 -9.7; 4788 -8.9; 5267 -9.9; 5793 -12.3; 6373 -13.6; 7010 -12.2; 7711 -7.8; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Elements Wireless Over-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Elements Wireless Over-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.88 | -4.9 dB |
| Peaking | 51 Hz   | 0.36 | -6.1 dB |
| Peaking | 180 Hz  | 1.37 | -4.9 dB |
| Peaking | 995 Hz  | 0.29 | 7.7 dB  |
| Peaking | 3539 Hz | 0.59 | -8.3 dB |
| Peaking | 383 Hz  | 4.06 | 2.7 dB  |
| Peaking | 1491 Hz | 1.08 | 8.0 dB  |
| Peaking | 1864 Hz | 0.5  | -7.6 dB |
| Peaking | 5542 Hz | 0.68 | 6.9 dB  |
| Peaking | 6376 Hz | 2.72 | -9.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.3 dB |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Elements%20Wireless%20Over-Ear/Monster%20Elements%20Wireless%20Over-Ear.png)