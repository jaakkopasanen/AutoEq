# Beats urBeats
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.4; 28 -8.5; 31 -8.6; 34 -8.6; 37 -8.7; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.4; 60 -9.8; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.1; 96 -11.6; 106 -12.1; 116 -12.6; 128 -13.1; 141 -13.4; 155 -13.5; 170 -13.5; 187 -13.3; 206 -13.2; 227 -13.1; 249 -13.0; 274 -12.5; 302 -11.8; 332 -11.1; 365 -10.4; 402 -9.6; 442 -8.8; 486 -8.0; 535 -7.0; 588 -5.9; 647 -4.8; 712 -3.7; 783 -2.8; 861 -2.5; 947 -2.4; 1042 -2.7; 1146 -3.0; 1261 -3.2; 1387 -3.1; 1526 -3.0; 1678 -3.1; 1846 -3.3; 2031 -3.4; 2234 -2.6; 2457 -1.5; 2703 -0.9; 2973 -1.2; 3270 -2.0; 3597 -3.0; 3957 -4.1; 4353 -5.7; 4788 -7.0; 5267 -8.3; 5793 -6.9; 6373 -3.4; 7010 -0.5; 7711 -2.3; 8482 -2.5; 9330 -2.8; 10263 -6.6; 11289 -3.8; 12418 -2.6; 13660 -2.6; 15026 -5.4; 16529 -3.0; 18182 -2.6; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats urBeats GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats urBeats ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.22 | -5.5 dB |
| Peaking | 163 Hz   | 0.73 | -7.1 dB |
| Peaking | 330 Hz   | 1.21 | -4.7 dB |
| Peaking | 5185 Hz  | 4.16 | -6.3 dB |
| Peaking | 10417 Hz | 7.22 | -4.4 dB |
| Peaking | 880 Hz   | 3.06 | 1.8 dB  |
| Peaking | 2826 Hz  | 2.19 | 4.3 dB  |
| Peaking | 2995 Hz  | 0.85 | -2.2 dB |
| Peaking | 7015 Hz  | 6.11 | 3.2 dB  |
| Peaking | 15209 Hz | 4.86 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | -9.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20urBeats/Beats%20urBeats.png)