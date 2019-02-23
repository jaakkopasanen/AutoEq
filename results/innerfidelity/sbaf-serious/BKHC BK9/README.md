# BKHC BK9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.6; 25 -8.1; 28 -8.5; 31 -8.9; 34 -9.2; 37 -9.4; 41 -9.6; 45 -9.9; 49 -10.0; 54 -10.2; 60 -10.3; 66 -10.5; 72 -10.7; 79 -10.9; 87 -10.9; 96 -10.9; 106 -11.4; 116 -11.4; 128 -10.5; 141 -10.8; 155 -11.0; 170 -11.0; 187 -11.1; 206 -11.5; 227 -12.0; 249 -12.3; 274 -12.4; 302 -12.4; 332 -12.7; 365 -13.0; 402 -13.4; 442 -13.6; 486 -14.0; 535 -14.2; 588 -14.0; 647 -14.1; 712 -13.9; 783 -12.9; 861 -11.6; 947 -11.3; 1042 -10.5; 1146 -9.1; 1261 -7.6; 1387 -6.5; 1526 -5.4; 1678 -4.6; 1846 -3.7; 2031 -3.0; 2234 -2.5; 2457 -2.6; 2703 -3.0; 2973 -2.7; 3270 -1.9; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BKHC BK9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BKHC BK9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.35 | -3.8 dB |
| Peaking | 611 Hz  | 0.56 | -7.7 dB |
| Peaking | 1964 Hz | 0.99 | 5.3 dB  |
| Peaking | 3789 Hz | 2.64 | 4.6 dB  |
| Peaking | 5769 Hz | 3.11 | 5.7 dB  |
| Peaking | 229 Hz  | 1.48 | 0.9 dB  |
| Peaking | 239 Hz  | 2.71 | -1.4 dB |
| Peaking | 8266 Hz | 4.37 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -7.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/BKHC%20BK9/BKHC%20BK9.png)