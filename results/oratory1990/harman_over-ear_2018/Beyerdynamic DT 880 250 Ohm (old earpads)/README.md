# Beyerdynamic DT 880 250 Ohm (old earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.9; 79 -1.6; 87 -2.3; 96 -3.0; 106 -3.6; 116 -4.2; 128 -4.7; 141 -5.2; 155 -5.6; 170 -5.9; 187 -6.1; 206 -6.3; 227 -6.5; 249 -6.5; 274 -6.5; 302 -6.4; 332 -6.3; 365 -6.2; 402 -6.2; 442 -6.1; 486 -5.9; 535 -5.8; 588 -5.9; 647 -5.9; 712 -6.1; 783 -6.2; 861 -6.4; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.2; 1387 -6.0; 1526 -6.0; 1678 -6.2; 1846 -6.3; 2031 -6.4; 2234 -6.4; 2457 -6.5; 2703 -6.7; 2973 -6.4; 3270 -5.4; 3597 -4.3; 3957 -4.2; 4353 -3.9; 4788 -2.9; 5267 -4.0; 5793 -7.9; 6373 -8.6; 7010 -6.9; 7711 -6.9; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -6.5; 15026 -6.5; 16529 -8.9; 18182 -13.1; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm (old earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm (old earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.51 | 6.8 dB  |
| Peaking | 577 Hz   | 3.37 | 0.6 dB  |
| Peaking | 1449 Hz  | 4.4  | 0.5 dB  |
| Peaking | 4485 Hz  | 3.4  | 3.6 dB  |
| Peaking | 19062 Hz | 1.06 | -8.3 dB |
| Peaking | 41 Hz    | 2.34 | -1.0 dB |
| Peaking | 71 Hz    | 3.62 | 1.2 dB  |
| Peaking | 5153 Hz  | 7.44 | 2.3 dB  |
| Peaking | 6074 Hz  | 5.16 | -3.3 dB |
| Peaking | 15017 Hz | 2.93 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20880%20250%20Ohm%20(old%20earpads)/Beyerdynamic%20DT%20880%20250%20Ohm%20(old%20earpads).png)