# Jabra Elite Active 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -1.8; 37 -2.2; 41 -2.6; 45 -3.0; 49 -3.2; 54 -3.5; 60 -4.1; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.6; 96 -6.1; 106 -6.7; 116 -7.3; 128 -7.8; 141 -8.1; 155 -8.5; 170 -8.7; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.4; 274 -8.1; 302 -7.7; 332 -7.4; 365 -7.2; 402 -6.9; 442 -6.3; 486 -5.7; 535 -5.1; 588 -4.4; 647 -3.7; 712 -3.2; 783 -3.6; 861 -4.2; 947 -4.5; 1042 -5.1; 1146 -5.8; 1261 -6.1; 1387 -6.1; 1526 -6.1; 1678 -6.4; 1846 -6.7; 2031 -6.9; 2234 -6.5; 2457 -5.9; 2703 -5.6; 2973 -5.5; 3270 -5.4; 3597 -5.5; 3957 -5.8; 4353 -6.7; 4788 -7.2; 5267 -7.0; 5793 -5.6; 6373 -4.4; 7010 -4.2; 7711 -6.2; 8482 -9.2; 9330 -12.5; 10263 -13.5; 11289 -10.7; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -8.5; 18182 -9.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Active 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Active 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.39 | 6.4 dB  |
| Peaking | 48 Hz    | 2.28 | 2.4 dB  |
| Peaking | 741 Hz   | 2.42 | 3.5 dB  |
| Peaking | 10075 Hz | 3.88 | -8.1 dB |
| Peaking | 17659 Hz | 2.73 | -4.3 dB |
| Peaking | 197 Hz   | 1.29 | -2.6 dB |
| Peaking | 3356 Hz  | 2.28 | 1.3 dB  |
| Peaking | 4953 Hz  | 2.78 | -1.6 dB |
| Peaking | 6673 Hz  | 2.83 | 3.5 dB  |
| Peaking | 8849 Hz  | 5.29 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Active%2065t/Jabra%20Elite%20Active%2065t.png)