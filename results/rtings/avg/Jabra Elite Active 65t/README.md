# Jabra Elite Active 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.0; 28 -1.9; 31 -2.8; 34 -3.4; 37 -3.9; 41 -4.3; 45 -4.6; 49 -4.9; 54 -5.2; 60 -5.7; 66 -6.2; 72 -6.5; 79 -6.8; 87 -7.3; 96 -7.8; 106 -8.4; 116 -9.0; 128 -9.4; 141 -9.8; 155 -10.2; 170 -10.3; 187 -10.4; 206 -10.3; 227 -10.2; 249 -10.1; 274 -9.8; 302 -9.4; 332 -9.1; 365 -8.8; 402 -8.6; 442 -8.0; 486 -7.4; 535 -6.8; 588 -6.1; 647 -5.3; 712 -4.9; 783 -5.2; 861 -5.8; 947 -6.2; 1042 -6.8; 1146 -7.5; 1261 -7.8; 1387 -7.8; 1526 -7.8; 1678 -8.0; 1846 -8.4; 2031 -8.6; 2234 -8.2; 2457 -7.6; 2703 -7.2; 2973 -7.1; 3270 -7.1; 3597 -7.2; 3957 -7.5; 4353 -8.3; 4788 -8.8; 5267 -8.7; 5793 -7.3; 6373 -6.1; 7010 -5.3; 7711 -7.4; 8482 -10.8; 9330 -14.2; 10263 -15.2; 11289 -12.4; 12418 -8.4; 13660 -6.5; 15026 -6.6; 16529 -10.2; 18182 -11.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Active 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Active 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.7  | 6.4 dB  |
| Peaking | 188 Hz   | 0.87 | -4.3 dB |
| Peaking | 1967 Hz  | 1.77 | -2.0 dB |
| Peaking | 10056 Hz | 2.97 | -9.6 dB |
| Peaking | 17702 Hz | 2.24 | -6.1 dB |
| Peaking | 376 Hz   | 2.4  | -0.8 dB |
| Peaking | 705 Hz   | 2.92 | 2.4 dB  |
| Peaking | 4875 Hz  | 3.38 | -2.2 dB |
| Peaking | 6896 Hz  | 5.32 | 2.9 dB  |
| Peaking | 19961 Hz | 2.58 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Active%2065t/Jabra%20Elite%20Active%2065t.png)