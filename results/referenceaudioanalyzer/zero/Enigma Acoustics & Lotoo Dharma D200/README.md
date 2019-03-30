# Enigma Acoustics & Lotoo Dharma D200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.6; 25 -9.0; 28 -9.6; 31 -10.0; 34 -10.4; 37 -10.7; 41 -11.0; 45 -11.3; 49 -11.5; 54 -11.7; 60 -11.8; 66 -12.0; 72 -12.1; 79 -12.1; 87 -12.1; 96 -12.1; 106 -12.1; 116 -12.1; 128 -12.1; 141 -11.8; 155 -11.8; 170 -11.6; 187 -11.3; 206 -11.1; 227 -10.8; 249 -10.5; 274 -10.1; 302 -9.7; 332 -9.3; 365 -8.8; 402 -8.2; 442 -7.6; 486 -7.0; 535 -6.3; 588 -5.5; 647 -4.8; 712 -4.0; 783 -3.1; 861 -2.2; 947 -1.3; 1042 -0.6; 1146 -0.5; 1261 -1.1; 1387 -2.0; 1526 -2.9; 1678 -3.4; 1846 -3.7; 2031 -4.0; 2234 -4.4; 2457 -4.8; 2703 -5.5; 2973 -6.3; 3270 -6.9; 3597 -7.2; 3957 -7.8; 4353 -9.1; 4788 -10.4; 5267 -11.6; 5793 -11.3; 6373 -8.9; 7010 -4.7; 7711 -6.0; 8482 -6.2; 9330 -6.2; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Enigma Acoustics & Lotoo Dharma D200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigma Acoustics & Lotoo Dharma D200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.81 | -1.3 dB |
| Peaking | 120 Hz  | 0.3  | -5.7 dB |
| Peaking | 1073 Hz | 0.93 | 6.3 dB  |
| Peaking | 5512 Hz | 1.9  | -6.6 dB |
| Peaking | 7016 Hz | 3.72 | 4.2 dB  |
| Peaking | 1544 Hz | 6.05 | -0.5 dB |
| Peaking | 2240 Hz | 4.91 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Enigma%20Acoustics%20&%20Lotoo%20Dharma%20D200/Enigma%20Acoustics%20&%20Lotoo%20Dharma%20D200.png)