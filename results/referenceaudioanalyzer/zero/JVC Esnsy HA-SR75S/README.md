# JVC Esnsy HA-SR75S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.8; 227 -1.5; 249 -2.4; 274 -3.2; 302 -4.0; 332 -4.7; 365 -5.3; 402 -5.6; 442 -5.9; 486 -6.2; 535 -6.5; 588 -6.9; 647 -7.3; 712 -7.8; 783 -8.2; 861 -8.6; 947 -8.9; 1042 -9.2; 1146 -9.4; 1261 -9.5; 1387 -9.5; 1526 -9.5; 1678 -9.5; 1846 -9.5; 2031 -9.4; 2234 -9.2; 2457 -8.8; 2703 -7.9; 2973 -7.0; 3270 -6.4; 3597 -6.3; 3957 -7.0; 4353 -8.3; 4788 -9.1; 5267 -9.2; 5793 -10.3; 6373 -12.0; 7010 -12.3; 7711 -11.0; 8482 -9.1; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC Esnsy HA-SR75S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC Esnsy HA-SR75S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.22 | 6.1 dB  |
| Peaking | 184 Hz   | 1.14 | 3.2 dB  |
| Peaking | 1111 Hz  | 0.93 | -3.0 dB |
| Peaking | 1979 Hz  | 2.44 | -1.9 dB |
| Peaking | 6767 Hz  | 2.32 | -6.1 dB |
| Peaking | 2478 Hz  | 5.09 | -0.8 dB |
| Peaking | 3507 Hz  | 2.65 | 1.5 dB  |
| Peaking | 4617 Hz  | 4.04 | -1.4 dB |
| Peaking | 10491 Hz | 3.88 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 5.3 dB  |
| Peaking | 250 Hz   | 1.41 | 3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20Esnsy%20HA-SR75S/JVC%20Esnsy%20HA-SR75S.png)