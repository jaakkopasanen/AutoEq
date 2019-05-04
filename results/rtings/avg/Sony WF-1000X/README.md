# Sony WF-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.7; 25 -2.8; 28 -2.8; 31 -2.8; 34 -2.9; 37 -2.9; 41 -3.0; 45 -3.1; 49 -3.2; 54 -3.3; 60 -3.5; 66 -3.8; 72 -4.0; 79 -4.3; 87 -4.6; 96 -4.9; 106 -5.1; 116 -5.2; 128 -5.3; 141 -5.1; 155 -5.0; 170 -4.9; 187 -4.7; 206 -4.4; 227 -4.0; 249 -3.8; 274 -3.7; 302 -3.9; 332 -4.0; 365 -4.2; 402 -4.4; 442 -4.4; 486 -4.2; 535 -3.9; 588 -3.5; 647 -3.0; 712 -2.5; 783 -2.1; 861 -1.6; 947 -1.1; 1042 -1.6; 1146 -2.2; 1261 -2.6; 1387 -2.7; 1526 -0.5; 1678 -1.1; 1846 -3.0; 2031 -4.1; 2234 -4.4; 2457 -4.0; 2703 -2.7; 2973 -1.2; 3270 -0.7; 3597 -0.7; 3957 -0.8; 4353 -0.9; 4788 -1.3; 5267 -1.7; 5793 -2.0; 6373 -2.1; 7010 -1.4; 7711 -2.5; 8482 -2.8; 9330 -2.8; 10263 -7.8; 11289 -10.1; 12418 -5.1; 13660 -2.8; 15026 -2.8; 16529 -2.8; 18182 -3.1; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 167 Hz   | 0.38 | -2.1 dB |
| Peaking | 909 Hz   | 4.69 | 1.5 dB  |
| Peaking | 2270 Hz  | 2.47 | -5.1 dB |
| Peaking | 2741 Hz  | 0.67 | 3.4 dB  |
| Peaking | 11168 Hz | 4.39 | -8.7 dB |
| Peaking | 259 Hz   | 3.45 | 1.0 dB  |
| Peaking | 457 Hz   | 3.34 | -0.7 dB |
| Peaking | 1379 Hz  | 4.5  | -1.3 dB |
| Peaking | 1560 Hz  | 7.99 | 2.5 dB  |
| Peaking | 13167 Hz | 6.89 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WF-1000X/Sony%20WF-1000X.png)