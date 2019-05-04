# Massdrop Plus Universal IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.0; 28 -3.1; 31 -3.2; 34 -3.3; 37 -3.4; 41 -3.5; 45 -3.6; 49 -3.8; 54 -3.9; 60 -4.1; 66 -4.3; 72 -4.6; 79 -4.9; 87 -5.1; 96 -5.4; 106 -5.6; 116 -5.8; 128 -5.9; 141 -5.9; 155 -5.9; 170 -5.9; 187 -5.7; 206 -5.5; 227 -5.2; 249 -4.9; 274 -4.6; 302 -4.2; 332 -3.8; 365 -3.4; 402 -3.0; 442 -2.9; 486 -2.6; 535 -2.3; 588 -2.0; 647 -1.7; 712 -1.3; 783 -1.1; 861 -1.1; 947 -1.3; 1042 -1.8; 1146 -2.5; 1261 -3.4; 1387 -4.1; 1526 -4.7; 1678 -5.0; 1846 -5.2; 2031 -5.4; 2234 -5.5; 2457 -5.1; 2703 -4.6; 2973 -4.0; 3270 -3.6; 3597 -3.4; 3957 -3.3; 4353 -3.2; 4788 -2.5; 5267 -1.3; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -6.4; 8482 -5.1; 9330 -3.7; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop Plus Universal IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop Plus Universal IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 150 Hz  | 0.82 | -2.5 dB |
| Peaking | 854 Hz  | 0.88 | 3.3 dB  |
| Peaking | 1795 Hz | 1.08 | -2.8 dB |
| Peaking | 6183 Hz | 2.01 | 4.3 dB  |
| Peaking | 7742 Hz | 3.93 | -4.9 dB |
| Peaking | 25 Hz   | 1.06 | 0.8 dB  |
| Peaking | 2394 Hz | 6.49 | -0.4 dB |
| Peaking | 3318 Hz | 4.39 | 0.5 dB  |
| Peaking | 7383 Hz | 0.92 | -0.2 dB |
| Peaking | 8990 Hz | 6.52 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Massdrop%20Plus%20Universal%20IEM/Massdrop%20Plus%20Universal%20IEM.png)