# AKG K712
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.1; 25 -3.5; 28 -3.9; 31 -4.3; 34 -4.6; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.8; 60 -6.1; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.3; 96 -7.7; 106 -8.0; 116 -8.2; 128 -8.3; 141 -8.5; 155 -8.8; 170 -9.0; 187 -9.3; 206 -9.7; 227 -9.9; 249 -9.9; 274 -9.7; 302 -9.6; 332 -9.3; 365 -9.1; 402 -8.9; 442 -8.7; 486 -8.5; 535 -8.0; 588 -7.4; 647 -6.7; 712 -6.2; 783 -5.6; 861 -4.9; 947 -4.1; 1042 -2.9; 1146 -1.6; 1261 -0.5; 1387 -1.1; 1526 -2.3; 1678 -3.6; 1846 -4.5; 2031 -5.8; 2234 -6.5; 2457 -4.7; 2703 -1.9; 2973 -0.8; 3270 -1.6; 3597 -2.5; 3957 -4.0; 4353 -5.3; 4788 -6.2; 5267 -8.7; 5793 -9.7; 6373 -7.2; 7010 -7.3; 7711 -7.3; 8482 -3.8; 9330 -3.4; 10263 -3.4; 11289 -5.1; 12418 -7.6; 13660 -4.7; 15026 -4.0; 16529 -8.8; 18182 -12.6; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 353 Hz   | 0.25 | -7.2 dB  |
| Peaking | 2003 Hz  | 0.5  | 10.5 dB  |
| Peaking | 2113 Hz  | 1.97 | -10.6 dB |
| Peaking | 5539 Hz  | 1.45 | -8.7 dB  |
| Peaking | 18929 Hz | 0.85 | -10.3 dB |
| Peaking | 18 Hz    | 2.35 | 1.2 dB   |
| Peaking | 793 Hz   | 3.72 | -0.4 dB  |
| Peaking | 10329 Hz | 3.06 | 2.3 dB   |
| Peaking | 12147 Hz | 3.23 | -3.9 dB  |
| Peaking | 14416 Hz | 3.87 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -4.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K712/AKG%20K712.png)