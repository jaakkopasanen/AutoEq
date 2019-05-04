# Beats urBeats
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.3; 25 -12.4; 28 -12.5; 31 -12.6; 34 -12.7; 37 -12.8; 41 -12.9; 45 -13.0; 49 -13.0; 54 -13.1; 60 -13.3; 66 -13.4; 72 -13.6; 79 -13.7; 87 -13.9; 96 -14.0; 106 -14.1; 116 -14.1; 128 -14.1; 141 -13.9; 155 -13.7; 170 -13.4; 187 -12.9; 206 -12.7; 227 -12.5; 249 -12.3; 274 -11.7; 302 -11.0; 332 -10.3; 365 -9.6; 402 -8.9; 442 -8.1; 486 -7.2; 535 -6.2; 588 -5.2; 647 -4.1; 712 -3.1; 783 -2.2; 861 -1.8; 947 -1.7; 1042 -2.0; 1146 -2.5; 1261 -2.6; 1387 -2.5; 1526 -2.4; 1678 -2.6; 1846 -2.9; 2031 -3.0; 2234 -2.6; 2457 -1.6; 2703 -0.8; 2973 -0.5; 3270 -1.0; 3597 -2.0; 3957 -3.1; 4353 -4.6; 4788 -6.6; 5267 -7.9; 5793 -6.0; 6373 -1.7; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats urBeats GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats urBeats ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.2  | -5.1 dB |
| Peaking | 209 Hz  | 0.31 | -6.6 dB |
| Peaking | 853 Hz  | 0.7  | 6.5 dB  |
| Peaking | 2955 Hz | 2.22 | 4.8 dB  |
| Peaking | 23 Hz   | 1.15 | -0.8 dB |
| Peaking | 1647 Hz | 6.45 | 0.5 dB  |
| Peaking | 3999 Hz | 3.12 | 1.7 dB  |
| Peaking | 5308 Hz | 2.39 | -4.1 dB |
| Peaking | 6494 Hz | 5.41 | 6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20urBeats/Beats%20urBeats.png)