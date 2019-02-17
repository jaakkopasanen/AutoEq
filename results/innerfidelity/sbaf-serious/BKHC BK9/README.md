# BKHC BK9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.1; 25 -3.5; 28 -4.0; 31 -4.3; 34 -4.6; 37 -4.9; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.6; 60 -5.8; 66 -6.0; 72 -6.1; 79 -6.3; 87 -6.3; 96 -6.3; 106 -6.9; 116 -6.8; 128 -6.0; 141 -6.3; 155 -6.5; 170 -6.5; 187 -6.6; 206 -6.9; 227 -7.5; 249 -7.7; 274 -7.9; 302 -7.9; 332 -8.1; 365 -8.5; 402 -8.8; 442 -9.0; 486 -9.4; 535 -9.7; 588 -9.5; 647 -9.6; 712 -9.4; 783 -8.4; 861 -7.1; 947 -6.7; 1042 -5.9; 1146 -4.5; 1261 -3.0; 1387 -1.9; 1526 -0.9; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BKHC BK9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BKHC BK9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.99 | 0.8 dB  |
| Peaking | 14 Hz   | 0.6  | 4.1 dB  |
| Peaking | 666 Hz  | 0.76 | -5.3 dB |
| Peaking | 1890 Hz | 0.61 | 7.3 dB  |
| Peaking | 5137 Hz | 1.82 | 4.4 dB  |
| Peaking | 2283 Hz | 2.54 | -1.1 dB |
| Peaking | 3842 Hz | 0.78 | 1.2 dB  |
| Peaking | 4903 Hz | 3.96 | -1.1 dB |
| Peaking | 6393 Hz | 4.02 | 3.6 dB  |
| Peaking | 7352 Hz | 1.42 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BKHC%20BK9/BKHC%20BK9.png)