# Monster Elements Wireless On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.6; 25 -10.8; 28 -11.0; 31 -11.2; 34 -11.3; 37 -11.4; 41 -11.4; 45 -11.5; 49 -11.5; 54 -11.5; 60 -11.5; 66 -11.5; 72 -11.6; 79 -11.6; 87 -11.6; 96 -11.6; 106 -11.6; 116 -11.6; 128 -11.6; 141 -11.3; 155 -10.8; 170 -10.0; 187 -8.7; 206 -7.1; 227 -5.3; 249 -3.9; 274 -3.1; 302 -3.1; 332 -3.3; 365 -3.5; 402 -3.5; 442 -3.9; 486 -4.4; 535 -4.9; 588 -5.3; 647 -5.8; 712 -6.2; 783 -6.6; 861 -7.0; 947 -7.4; 1042 -7.7; 1146 -8.0; 1261 -8.2; 1387 -8.3; 1526 -8.3; 1678 -8.5; 1846 -8.7; 2031 -8.7; 2234 -8.5; 2457 -8.3; 2703 -8.5; 2973 -8.3; 3270 -7.1; 3597 -6.3; 3957 -8.4; 4353 -10.2; 4788 -9.8; 5267 -7.2; 5793 -3.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Elements Wireless On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Elements Wireless On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.25 | -5.6 dB |
| Peaking | 161 Hz  | 1.04 | -5.5 dB |
| Peaking | 265 Hz  | 0.73 | 7.4 dB  |
| Peaking | 2213 Hz | 0.32 | -2.9 dB |
| Peaking | 6364 Hz | 4.96 | 7.8 dB  |
| Peaking | 3559 Hz | 5.61 | 2.6 dB  |
| Peaking | 4535 Hz | 4.11 | -3.5 dB |
| Peaking | 8199 Hz | 0.58 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Monster%20Elements%20Wireless%20On-Ear/Monster%20Elements%20Wireless%20On-Ear.png)