# Beats UrBeats
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -14.1; 25 -14.6; 28 -15.2; 31 -15.6; 34 -16.0; 37 -16.2; 41 -16.5; 45 -16.7; 49 -16.8; 54 -16.8; 60 -16.8; 66 -16.8; 72 -16.8; 79 -16.8; 87 -16.8; 96 -16.6; 106 -16.4; 116 -16.2; 128 -15.9; 141 -15.6; 155 -15.2; 170 -14.9; 187 -14.5; 206 -14.1; 227 -13.7; 249 -13.1; 274 -12.5; 302 -11.9; 332 -11.3; 365 -10.8; 402 -10.4; 442 -9.7; 486 -8.9; 535 -8.1; 588 -7.4; 647 -6.7; 712 -5.9; 783 -5.2; 861 -4.4; 947 -3.7; 1042 -3.2; 1146 -2.7; 1261 -2.2; 1387 -1.9; 1526 -1.8; 1678 -1.8; 1846 -2.0; 2031 -2.5; 2234 -3.2; 2457 -3.7; 2703 -3.6; 2973 -3.1; 3270 -2.6; 3597 -2.5; 3957 -2.5; 4353 -2.5; 4788 -2.5; 5267 -2.5; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats UrBeats GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats UrBeats ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.47 | -5.0 dB |
| Peaking | 113 Hz  | 0.28 | -9.1 dB |
| Peaking | 1345 Hz | 0.76 | 4.8 dB  |
| Peaking | 4165 Hz | 1.74 | 2.8 dB  |
| Peaking | 6249 Hz | 4.85 | 4.5 dB  |
| Peaking | 2601 Hz | 3.5  | -1.6 dB |
| Peaking | 2733 Hz | 1.53 | 1.3 dB  |
| Peaking | 5514 Hz | 3.03 | 2.1 dB  |
| Peaking | 5734 Hz | 1.12 | -2.1 dB |
| Peaking | 6644 Hz | 7.75 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB |
| Peaking | 62 Hz    | 1.41 | -8.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20UrBeats/Beats%20UrBeats.png)