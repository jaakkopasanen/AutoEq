# Beats Fake UrBeats
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.9; 25 -14.3; 28 -14.8; 31 -15.2; 34 -15.6; 37 -15.8; 41 -16.1; 45 -16.2; 49 -16.4; 54 -16.5; 60 -16.7; 66 -16.7; 72 -16.7; 79 -16.7; 87 -16.7; 96 -16.7; 106 -16.7; 116 -16.7; 128 -16.6; 141 -16.3; 155 -16.4; 170 -16.2; 187 -16.0; 206 -15.9; 227 -15.7; 249 -15.5; 274 -15.2; 302 -14.8; 332 -14.4; 365 -14.0; 402 -13.4; 442 -12.8; 486 -12.0; 535 -11.1; 588 -10.1; 647 -9.0; 712 -7.9; 783 -6.6; 861 -5.3; 947 -3.9; 1042 -2.3; 1146 -0.8; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -3.0; 4788 -5.0; 5267 -7.6; 5793 -10.2; 6373 -10.3; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Fake UrBeats GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Fake UrBeats ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 69 Hz    | 0.19 | -9.8 dB  |
| Peaking | 525 Hz   | 0.48 | -10.4 dB |
| Peaking | 1031 Hz  | 0.32 | 9.1 dB   |
| Peaking | 1704 Hz  | 0.3  | 2.7 dB   |
| Peaking | 5964 Hz  | 3.19 | -7.5 dB  |
| Peaking | 814 Hz   | 2.44 | -0.5 dB  |
| Peaking | 1169 Hz  | 3.72 | 1.5 dB   |
| Peaking | 1948 Hz  | 1.61 | -0.9 dB  |
| Peaking | 3710 Hz  | 4.33 | 1.6 dB   |
| Peaking | 10482 Hz | 1.69 | -0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -7.3 dB |
| Peaking | 500 Hz   | 1.41 | -5.3 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beats%20Fake%20UrBeats/Beats%20Fake%20UrBeats.png)