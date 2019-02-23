# AKG K712 (Dekoni Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.5; 41 -5.8; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.7; 72 -6.9; 79 -7.2; 87 -7.4; 96 -7.7; 106 -8.1; 116 -8.5; 128 -8.9; 141 -9.4; 155 -9.7; 170 -10.0; 187 -10.2; 206 -10.3; 227 -10.4; 249 -10.3; 274 -10.1; 302 -9.7; 332 -9.2; 365 -8.6; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.4; 588 -5.5; 647 -4.8; 712 -4.9; 783 -5.2; 861 -5.5; 947 -5.5; 1042 -5.1; 1146 -4.5; 1261 -3.7; 1387 -4.0; 1526 -5.0; 1678 -6.6; 1846 -7.8; 2031 -9.2; 2234 -10.3; 2457 -9.9; 2703 -7.8; 2973 -3.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.0; 5267 -7.4; 5793 -8.6; 6373 -5.8; 7010 -7.2; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -7.9; 13660 -6.6; 15026 -6.8; 16529 -10.4; 18182 -13.6; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 (Dekoni Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 (Dekoni Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.06 | 3.0 dB  |
| Peaking | 202 Hz   | 1.04 | -4.3 dB |
| Peaking | 2379 Hz  | 3.73 | -6.2 dB |
| Peaking | 3588 Hz  | 2.14 | 7.5 dB  |
| Peaking | 19124 Hz | 0.88 | -8.5 dB |
| Peaking | 684 Hz   | 3.25 | 2.2 dB  |
| Peaking | 1276 Hz  | 3.66 | 3.0 dB  |
| Peaking | 4565 Hz  | 5.87 | 3.1 dB  |
| Peaking | 5491 Hz  | 4.37 | -4.0 dB |
| Peaking | 14617 Hz | 4.52 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712%20(Dekoni%20Sheepskin%20Earpads)/AKG%20K712%20(Dekoni%20Sheepskin%20Earpads).png)