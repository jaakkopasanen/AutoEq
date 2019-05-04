# Sony WH-CH500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -2.6; 37 -4.3; 41 -6.3; 45 -7.9; 49 -9.1; 54 -10.2; 60 -11.2; 66 -11.8; 72 -12.1; 79 -12.0; 87 -11.7; 96 -11.3; 106 -10.8; 116 -10.2; 128 -9.6; 141 -8.9; 155 -8.2; 170 -7.7; 187 -7.2; 206 -6.8; 227 -6.6; 249 -6.3; 274 -6.2; 302 -6.1; 332 -6.1; 365 -5.9; 402 -5.4; 442 -5.5; 486 -6.1; 535 -6.6; 588 -6.7; 647 -6.4; 712 -6.2; 783 -6.3; 861 -6.4; 947 -6.8; 1042 -6.9; 1146 -6.8; 1261 -7.2; 1387 -7.4; 1526 -7.5; 1678 -7.3; 1846 -7.2; 2031 -7.2; 2234 -6.7; 2457 -6.1; 2703 -6.3; 2973 -6.8; 3270 -6.7; 3597 -6.3; 3957 -3.9; 4353 -0.8; 4788 -0.5; 5267 -2.0; 5793 -1.5; 6373 -2.8; 7010 -6.3; 7711 -9.7; 8482 -10.3; 9330 -10.6; 10263 -9.9; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WH-CH500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WH-CH500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.86 | 9.3 dB  |
| Peaking | 65 Hz   | 0.66 | -8.0 dB |
| Peaking | 260 Hz  | 0.91 | 1.5 dB  |
| Peaking | 5217 Hz | 2.06 | 6.8 dB  |
| Peaking | 8743 Hz | 2.18 | -5.5 dB |
| Peaking | 422 Hz  | 7.32 | 0.9 dB  |
| Peaking | 1603 Hz | 1.53 | -1.1 dB |
| Peaking | 2548 Hz | 5.22 | 0.7 dB  |
| Peaking | 3484 Hz | 2.26 | -1.7 dB |
| Peaking | 4321 Hz | 6.5  | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -7.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WH-CH500/Sony%20WH-CH500.png)