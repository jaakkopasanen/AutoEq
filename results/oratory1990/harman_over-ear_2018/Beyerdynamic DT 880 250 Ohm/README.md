# Beyerdynamic DT880 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.8; 49 -1.0; 54 -1.2; 60 -1.5; 66 -1.8; 72 -1.9; 79 -1.7; 87 -2.2; 96 -3.4; 106 -4.1; 116 -4.6; 128 -5.0; 141 -5.4; 155 -5.7; 170 -5.9; 187 -6.2; 206 -6.3; 227 -6.4; 249 -6.4; 274 -6.3; 302 -6.2; 332 -6.1; 365 -6.0; 402 -5.9; 442 -5.9; 486 -5.6; 535 -5.4; 588 -5.6; 647 -5.5; 712 -5.4; 783 -5.4; 861 -5.9; 947 -6.2; 1042 -6.2; 1146 -6.0; 1261 -6.0; 1387 -6.2; 1526 -6.1; 1678 -6.3; 1846 -6.4; 2031 -6.4; 2234 -6.5; 2457 -7.0; 2703 -7.9; 2973 -8.2; 3270 -7.6; 3597 -6.9; 3957 -7.3; 4353 -7.0; 4788 -6.3; 5267 -8.2; 5793 -12.6; 6373 -11.6; 7010 -8.3; 7711 -7.7; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -7.8; 12418 -8.5; 13660 -6.7; 15026 -7.1; 16529 -11.6; 18182 -15.4; 20000 -17.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.48 | 6.4 dB   |
| Peaking | 2902 Hz  | 2.57 | -2.3 dB  |
| Peaking | 5241 Hz  | 0.1  | 0.8 dB   |
| Peaking | 6049 Hz  | 4.48 | -7.3 dB  |
| Peaking | 19320 Hz | 0.72 | -11.6 dB |
| Peaking | 82 Hz    | 4.79 | 1.5 dB   |
| Peaking | 188 Hz   | 1.54 | -0.8 dB  |
| Peaking | 12223 Hz | 4.53 | -2.0 dB  |
| Peaking | 14659 Hz | 2.34 | 2.5 dB   |
| Peaking | 17258 Hz | 2.72 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT880%20250%20Ohm.png)