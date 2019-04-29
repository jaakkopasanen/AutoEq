# BGVP DM6 20 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.4; 25 -2.9; 28 -3.6; 31 -4.1; 34 -4.6; 37 -5.0; 41 -5.4; 45 -5.9; 49 -6.3; 54 -6.7; 60 -7.1; 66 -7.6; 72 -8.0; 79 -8.5; 87 -9.0; 96 -9.5; 106 -9.9; 116 -10.4; 128 -10.8; 141 -11.1; 155 -11.3; 170 -11.5; 187 -11.7; 206 -11.8; 227 -11.9; 249 -11.8; 274 -11.7; 302 -11.6; 332 -11.3; 365 -11.0; 402 -10.8; 442 -10.5; 486 -10.2; 535 -9.8; 588 -9.4; 647 -8.9; 712 -8.3; 783 -7.8; 861 -7.3; 947 -7.0; 1042 -7.1; 1146 -7.5; 1261 -7.9; 1387 -7.8; 1526 -7.1; 1678 -6.2; 1846 -5.0; 2031 -3.6; 2234 -2.0; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.7; 4788 -2.8; 5267 -0.6; 5793 -0.7; 6373 -3.6; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.0; 15026 -25.6; 16529 -29.7; 18182 -23.0; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 20 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 20 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 228 Hz   | 0.3  | -5.3 dB  |
| Peaking | 4526 Hz  | 0.52 | 8.0 dB   |
| Peaking | 12569 Hz | 1.7  | 13.0 dB  |
| Peaking | 16099 Hz | 0.84 | -28.6 dB |
| Peaking | 17 Hz    | 0.65 | 5.6 dB   |
| Peaking | 64 Hz    | 1.4  | 0.9 dB   |
| Peaking | 1509 Hz  | 1.55 | -5.5 dB  |
| Peaking | 1783 Hz  | 0.61 | 3.4 dB   |
| Peaking | 4395 Hz  | 6.49 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 16000 Hz | 1.41 | -23.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DM6%2020%20Ohm/BGVP%20DM6%2020%20Ohm.png)