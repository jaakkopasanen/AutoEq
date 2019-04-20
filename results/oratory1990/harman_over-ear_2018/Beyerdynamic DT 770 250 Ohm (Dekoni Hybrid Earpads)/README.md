# Beyerdynamic DT 770 250 Ohm (Dekoni Hybrid Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.2; 28 -8.4; 31 -8.6; 34 -8.7; 37 -8.8; 41 -8.8; 45 -8.8; 49 -8.7; 54 -8.6; 60 -8.4; 66 -8.1; 72 -8.0; 79 -7.8; 87 -7.4; 96 -6.9; 106 -6.6; 116 -6.5; 128 -6.3; 141 -5.6; 155 -4.3; 170 -2.9; 187 -1.6; 206 -0.6; 227 -0.5; 249 -1.2; 274 -2.5; 302 -3.7; 332 -4.8; 365 -5.7; 402 -6.6; 442 -7.4; 486 -7.8; 535 -8.0; 588 -8.1; 647 -8.2; 712 -8.5; 783 -8.8; 861 -8.9; 947 -8.8; 1042 -8.5; 1146 -8.2; 1261 -7.8; 1387 -7.5; 1526 -7.4; 1678 -7.3; 1846 -7.5; 2031 -7.9; 2234 -8.3; 2457 -8.7; 2703 -8.6; 2973 -7.6; 3270 -6.0; 3597 -3.3; 3957 -2.4; 4353 -3.3; 4788 -6.5; 5267 -11.1; 5793 -11.6; 6373 -8.3; 7010 -4.4; 7711 -6.5; 8482 -9.5; 9330 -9.8; 10263 -10.0; 11289 -12.4; 12418 -13.1; 13660 -11.9; 15026 -14.1; 16529 -17.9; 18182 -18.1; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 250 Ohm (Dekoni Hybrid Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 250 Ohm (Dekoni Hybrid Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 208 Hz   | 0.08 | -2.6 dB  |
| Peaking | 219 Hz   | 1.25 | 8.8 dB   |
| Peaking | 4057 Hz  | 3.28 | 6.0 dB   |
| Peaking | 5533 Hz  | 6.56 | -5.9 dB  |
| Peaking | 17930 Hz | 0.51 | -12.1 dB |
| Peaking | 1555 Hz  | 3.22 | 1.1 dB   |
| Peaking | 2599 Hz  | 4.43 | -1.6 dB  |
| Peaking | 6214 Hz  | 4.4  | -1.9 dB  |
| Peaking | 7002 Hz  | 5.71 | 5.0 dB   |
| Peaking | 11707 Hz | 5.47 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB   |
| Peaking | 250 Hz   | 1.41 | 6.4 dB   |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -14.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20770%20250%20Ohm%20(Dekoni%20Hybrid%20Earpads)/Beyerdynamic%20DT%20770%20250%20Ohm%20(Dekoni%20Hybrid%20Earpads).png)