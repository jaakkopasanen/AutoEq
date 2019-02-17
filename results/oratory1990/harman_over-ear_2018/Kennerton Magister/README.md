# Kennerton Magister
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.4; 25 -3.9; 28 -4.5; 31 -4.9; 34 -5.2; 37 -5.5; 41 -5.9; 45 -6.2; 49 -6.5; 54 -6.8; 60 -6.7; 66 -6.1; 72 -5.7; 79 -7.1; 87 -9.2; 96 -9.2; 106 -10.6; 116 -11.5; 128 -12.0; 141 -12.3; 155 -12.3; 170 -12.0; 187 -11.6; 206 -11.5; 227 -10.3; 249 -8.3; 274 -5.5; 302 -2.0; 332 -0.5; 365 -0.6; 402 -2.9; 442 -4.8; 486 -5.4; 535 -6.4; 588 -7.0; 647 -7.0; 712 -6.6; 783 -6.1; 861 -6.1; 947 -6.3; 1042 -6.3; 1146 -5.9; 1261 -5.3; 1387 -4.6; 1526 -3.9; 1678 -3.2; 1846 -2.9; 2031 -2.5; 2234 -2.6; 2457 -3.8; 2703 -5.1; 2973 -5.9; 3270 -6.2; 3597 -1.7; 3957 -5.3; 4353 -7.6; 4788 -10.7; 5267 -13.2; 5793 -12.4; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.6; 15026 -14.0; 16529 -15.4; 18182 -12.8; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Magister GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Magister ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 168 Hz   | 1    | -6.8 dB  |
| Peaking | 334 Hz   | 2.85 | 8.8 dB   |
| Peaking | 4871 Hz  | 0.32 | 3.8 dB   |
| Peaking | 5244 Hz  | 3.58 | -11.1 dB |
| Peaking | 16547 Hz | 0.99 | -10.2 dB |
| Peaking | 12 Hz    | 1.16 | 1.1 dB   |
| Peaking | 13 Hz    | 0.64 | 4.5 dB   |
| Peaking | 2039 Hz  | 2.91 | 2.4 dB   |
| Peaking | 3255 Hz  | 2.37 | -3.5 dB  |
| Peaking | 3669 Hz  | 9.34 | 6.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -9.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Kennerton%20Magister/Kennerton%20Magister.png)