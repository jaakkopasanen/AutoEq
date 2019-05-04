# Beyerdynamic DT 1770 (Velours Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.7; 25 -10.8; 28 -11.0; 31 -11.0; 34 -11.0; 37 -10.8; 41 -10.6; 45 -10.5; 49 -10.4; 54 -9.6; 60 -8.5; 66 -8.6; 72 -10.0; 79 -11.0; 87 -11.7; 96 -12.3; 106 -12.7; 116 -13.2; 128 -13.0; 141 -12.5; 155 -11.7; 170 -11.0; 187 -9.4; 206 -7.3; 227 -5.7; 249 -5.1; 274 -5.4; 302 -6.2; 332 -6.9; 365 -7.3; 402 -7.7; 442 -7.9; 486 -7.9; 535 -7.8; 588 -7.3; 647 -6.8; 712 -6.7; 783 -6.6; 861 -6.8; 947 -7.3; 1042 -7.4; 1146 -6.8; 1261 -6.1; 1387 -5.3; 1526 -4.4; 1678 -2.8; 1846 -1.2; 2031 -0.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.0; 3597 -2.2; 3957 -0.7; 4353 -0.5; 4788 -5.1; 5267 -8.8; 5793 -10.4; 6373 -10.8; 7010 -10.5; 7711 -12.2; 8482 -11.6; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 (Velours Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 (Velours Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.73 | -4.5 dB |
| Peaking | 119 Hz  | 1.52 | -6.7 dB |
| Peaking | 2473 Hz | 1.43 | 7.1 dB  |
| Peaking | 4253 Hz | 3.42 | 7.1 dB  |
| Peaking | 6509 Hz | 1.27 | -6.4 dB |
| Peaking | 174 Hz  | 3.47 | -2.4 dB |
| Peaking | 243 Hz  | 1.66 | 4.1 dB  |
| Peaking | 403 Hz  | 0.65 | -1.8 dB |
| Peaking | 8388 Hz | 4.37 | -4.8 dB |
| Peaking | 9096 Hz | 1.67 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201770%20(Velours%20Earpads)/Beyerdynamic%20DT%201770%20(Velours%20Earpads).png)