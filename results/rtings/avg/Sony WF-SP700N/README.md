# Sony WF-SP700N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.4; 25 -14.7; 28 -15.1; 31 -15.3; 34 -15.5; 37 -15.6; 41 -15.5; 45 -15.5; 49 -15.4; 54 -15.2; 60 -15.0; 66 -14.7; 72 -14.4; 79 -14.1; 87 -13.7; 96 -13.3; 106 -12.9; 116 -12.4; 128 -11.9; 141 -11.3; 155 -10.9; 170 -10.4; 187 -9.7; 206 -9.1; 227 -8.4; 249 -7.8; 274 -7.1; 302 -6.5; 332 -6.0; 365 -5.5; 402 -5.0; 442 -4.6; 486 -4.1; 535 -3.6; 588 -3.0; 647 -2.4; 712 -1.7; 783 -1.2; 861 -1.1; 947 -1.7; 1042 -2.8; 1146 -3.8; 1261 -4.4; 1387 -4.9; 1526 -5.2; 1678 -5.5; 1846 -5.8; 2031 -6.0; 2234 -5.6; 2457 -4.6; 2703 -3.6; 2973 -2.8; 3270 -2.4; 3597 -2.2; 3957 -1.9; 4353 -1.5; 4788 -1.1; 5267 -0.5; 5793 -1.8; 6373 -7.3; 7010 -5.4; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -10.9; 11289 -11.4; 12418 -5.8; 13660 -5.0; 15026 -5.0; 16529 -7.2; 18182 -11.8; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WF-SP700N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WF-SP700N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.45 | -10.6 dB |
| Peaking | 118 Hz   | 0.97 | -3.8 dB  |
| Peaking | 4449 Hz  | 1.64 | 4.2 dB   |
| Peaking | 10817 Hz | 4.83 | -8.2 dB  |
| Peaking | 18372 Hz | 1.86 | -7.7 dB  |
| Peaking | 810 Hz   | 1.46 | 4.6 dB   |
| Peaking | 3007 Hz  | 1.98 | 4.7 dB   |
| Peaking | 3175 Hz  | 0.7  | -4.5 dB  |
| Peaking | 6052 Hz  | 1.68 | 5.4 dB   |
| Peaking | 6477 Hz  | 5.69 | -7.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WF-SP700N/Sony%20WF-SP700N.png)