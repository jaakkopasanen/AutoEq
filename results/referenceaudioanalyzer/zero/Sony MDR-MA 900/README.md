# Sony MDR-MA 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.4; 49 -2.3; 54 -3.2; 60 -4.5; 66 -5.7; 72 -6.6; 79 -7.2; 87 -7.7; 96 -8.1; 106 -8.3; 116 -8.3; 128 -8.3; 141 -8.3; 155 -8.5; 170 -8.4; 187 -8.3; 206 -8.1; 227 -7.7; 249 -7.2; 274 -6.6; 302 -6.3; 332 -6.0; 365 -6.0; 402 -6.0; 442 -6.0; 486 -6.0; 535 -5.7; 588 -5.5; 647 -5.6; 712 -5.9; 783 -6.2; 861 -6.7; 947 -7.3; 1042 -7.9; 1146 -7.9; 1261 -6.7; 1387 -4.0; 1526 -1.9; 1678 -2.4; 1846 -3.7; 2031 -4.1; 2234 -3.4; 2457 -2.4; 2703 -1.5; 2973 -0.9; 3270 -0.7; 3597 -1.5; 3957 -4.0; 4353 -7.3; 4788 -9.9; 5267 -11.0; 5793 -10.7; 6373 -10.1; 7010 -9.9; 7711 -10.4; 8482 -10.8; 9330 -10.7; 10263 -9.7; 11289 -8.1; 12418 -7.0; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-MA 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-MA 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 1.38 | 7.4 dB  |
| Peaking | 1580 Hz  | 5.79 | 4.2 dB  |
| Peaking | 3285 Hz  | 1.5  | 7.9 dB  |
| Peaking | 5117 Hz  | 1.75 | -6.5 dB |
| Peaking | 8885 Hz  | 1.88 | -4.1 dB |
| Peaking | 50 Hz    | 2.32 | 2.8 dB  |
| Peaking | 137 Hz   | 0.57 | -3.2 dB |
| Peaking | 429 Hz   | 0.34 | 1.6 dB  |
| Peaking | 1064 Hz  | 2.75 | -3.1 dB |
| Peaking | 13738 Hz | 2.79 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-MA%20900/Sony%20MDR-MA%20900.png)