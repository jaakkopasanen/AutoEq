# Shozy x AAW Pola
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.4; 25 -10.7; 28 -10.9; 31 -11.1; 34 -11.2; 37 -11.3; 41 -11.4; 45 -11.6; 49 -11.6; 54 -11.7; 60 -11.9; 66 -12.1; 72 -12.3; 79 -12.5; 87 -12.7; 96 -12.9; 106 -13.1; 116 -13.2; 128 -13.4; 141 -13.5; 155 -13.5; 170 -13.5; 187 -13.4; 206 -13.1; 227 -13.0; 249 -12.7; 274 -12.6; 302 -12.4; 332 -12.1; 365 -12.0; 402 -11.9; 442 -11.8; 486 -11.8; 535 -11.7; 588 -11.5; 647 -11.3; 712 -11.3; 783 -10.7; 861 -10.5; 947 -10.7; 1042 -11.0; 1146 -11.4; 1261 -11.6; 1387 -11.2; 1526 -9.8; 1678 -7.6; 1846 -4.8; 2031 -1.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -10.9; 13660 -18.2; 15026 -26.3; 16529 -32.1; 18182 -29.8; 20000 -15.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy x AAW Pola GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy x AAW Pola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.22 | -3.4 dB  |
| Peaking | 317 Hz   | 0.23 | -6.5 dB  |
| Peaking | 1299 Hz  | 1.67 | -7.6 dB  |
| Peaking | 6540 Hz  | 0.21 | 14.2 dB  |
| Peaking | 16768 Hz | 0.56 | -35.0 dB |
| Peaking | 2115 Hz  | 1.51 | -2.6 dB  |
| Peaking | 2176 Hz  | 3.1  | 4.8 dB   |
| Peaking | 7842 Hz  | 4.89 | -2.9 dB  |
| Peaking | 11536 Hz | 3.06 | 5.1 dB   |
| Peaking | 14766 Hz | 3.1  | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 16000 Hz | 1.41 | -30.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Shozy%20x%20AAW%20Pola/Shozy%20x%20AAW%20Pola.png)