# AudioQuest NightOwl Stock Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.2; 25 -9.2; 28 -9.1; 31 -9.0; 34 -8.9; 37 -8.8; 41 -8.7; 45 -8.7; 49 -8.6; 54 -8.4; 60 -8.3; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.7; 96 -11.0; 106 -11.0; 116 -11.1; 128 -11.9; 141 -12.0; 155 -11.5; 170 -11.2; 187 -11.7; 206 -11.4; 227 -11.1; 249 -10.8; 274 -10.4; 302 -10.1; 332 -9.7; 365 -9.4; 402 -9.1; 442 -8.7; 486 -8.9; 535 -8.8; 588 -8.4; 647 -8.2; 712 -7.8; 783 -7.7; 861 -8.1; 947 -8.2; 1042 -8.1; 1146 -7.7; 1261 -7.2; 1387 -7.0; 1526 -6.3; 1678 -5.0; 1846 -3.5; 2031 -2.0; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -1.0; 3270 -2.2; 3597 -2.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.5; 6373 -5.4; 7010 -4.2; 7711 -6.2; 8482 -7.4; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AudioQuest NightOwl Stock Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioQuest NightOwl Stock Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.1  | -2.6 dB |
| Peaking | 163 Hz   | 0.62 | -5.2 dB |
| Peaking | 2432 Hz  | 1.28 | 8.9 dB  |
| Peaking | 2738 Hz  | 0.3  | -3.8 dB |
| Peaking | 4813 Hz  | 1.56 | 8.0 dB  |
| Peaking | 137 Hz   | 2.72 | -0.6 dB |
| Peaking | 163 Hz   | 7.87 | 1.2 dB  |
| Peaking | 8987 Hz  | 7.08 | -2.6 dB |
| Peaking | 10250 Hz | 1.32 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioQuest%20NightOwl%20Stock%20Pads/AudioQuest%20NightOwl%20Stock%20Pads.png)