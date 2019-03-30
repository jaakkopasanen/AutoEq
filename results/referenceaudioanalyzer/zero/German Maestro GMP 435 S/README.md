# German Maestro GMP 435 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.8; 41 -2.6; 45 -3.3; 49 -4.0; 54 -4.8; 60 -5.6; 66 -6.3; 72 -6.8; 79 -7.2; 87 -7.5; 96 -7.7; 106 -8.0; 116 -8.0; 128 -8.0; 141 -8.0; 155 -8.0; 170 -8.0; 187 -8.0; 206 -7.7; 227 -7.5; 249 -7.3; 274 -7.0; 302 -6.9; 332 -6.7; 365 -6.7; 402 -6.7; 442 -6.4; 486 -6.1; 535 -5.7; 588 -5.7; 647 -5.5; 712 -5.4; 783 -5.4; 861 -5.3; 947 -5.1; 1042 -5.0; 1146 -5.4; 1261 -5.9; 1387 -6.3; 1526 -6.5; 1678 -5.2; 1846 -3.1; 2031 -3.4; 2234 -4.8; 2457 -5.1; 2703 -5.0; 2973 -4.4; 3270 -3.2; 3597 -1.0; 3957 -0.5; 4353 -3.3; 4788 -6.5; 5267 -8.2; 5793 -10.0; 6373 -11.4; 7010 -12.3; 7711 -12.8; 8482 -11.5; 9330 -8.5; 10263 -6.9; 11289 -8.7; 12418 -11.2; 13660 -10.7; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`German Maestro GMP 435 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `German Maestro GMP 435 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.46 | 7.0 dB  |
| Peaking | 1937 Hz  | 3.99 | 3.4 dB  |
| Peaking | 3828 Hz  | 2.99 | 7.2 dB  |
| Peaking | 7081 Hz  | 1.79 | -6.8 dB |
| Peaking | 12998 Hz | 3.73 | -5.1 dB |
| Peaking | 15 Hz    | 2.88 | 2.4 dB  |
| Peaking | 44 Hz    | 2.07 | 1.6 dB  |
| Peaking | 129 Hz   | 0.65 | -1.8 dB |
| Peaking | 782 Hz   | 1.35 | 1.4 dB  |
| Peaking | 15835 Hz | 3.42 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/German%20Maestro%20GMP%20435%20S/German%20Maestro%20GMP%20435%20S.png)