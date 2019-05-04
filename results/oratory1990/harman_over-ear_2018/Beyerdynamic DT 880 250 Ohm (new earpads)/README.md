# Beyerdynamic DT 880 250 Ohm (new earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.0; 49 -1.2; 54 -1.4; 60 -1.7; 66 -2.0; 72 -2.1; 79 -2.0; 87 -2.5; 96 -3.6; 106 -4.3; 116 -4.8; 128 -5.2; 141 -5.6; 155 -5.9; 170 -6.2; 187 -6.4; 206 -6.5; 227 -6.6; 249 -6.6; 274 -6.5; 302 -6.4; 332 -6.3; 365 -6.2; 402 -6.1; 442 -6.1; 486 -5.8; 535 -5.6; 588 -5.7; 647 -5.6; 712 -5.5; 783 -5.6; 861 -6.0; 947 -6.4; 1042 -6.4; 1146 -6.2; 1261 -6.1; 1387 -6.2; 1526 -6.3; 1678 -6.4; 1846 -6.6; 2031 -6.5; 2234 -6.6; 2457 -7.1; 2703 -7.8; 2973 -8.1; 3270 -7.4; 3597 -6.7; 3957 -7.1; 4353 -7.2; 4788 -6.8; 5267 -8.2; 5793 -11.9; 6373 -11.3; 7010 -7.6; 7711 -6.9; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.8; 12418 -8.4; 13660 -7.4; 15026 -7.3; 16529 -10.7; 18182 -14.5; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm (new earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm (new earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.49 | 6.4 dB   |
| Peaking | 2869 Hz  | 1.92 | -2.0 dB  |
| Peaking | 6028 Hz  | 4.73 | -6.8 dB  |
| Peaking | 6133 Hz  | 0.12 | 0.8 dB   |
| Peaking | 19428 Hz | 0.69 | -10.8 dB |
| Peaking | 82 Hz    | 2.27 | 1.9 dB   |
| Peaking | 248 Hz   | 0.23 | -1.0 dB  |
| Peaking | 560 Hz   | 1.07 | 1.4 dB   |
| Peaking | 12444 Hz | 6.25 | -1.5 dB  |
| Peaking | 14681 Hz | 4.2  | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20880%20250%20Ohm%20(new%20earpads)/Beyerdynamic%20DT%20880%20250%20Ohm%20(new%20earpads).png)