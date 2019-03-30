# German Maestro GMP 450 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.6; 28 -2.7; 31 -3.6; 34 -4.3; 37 -4.8; 41 -5.3; 45 -5.8; 49 -6.1; 54 -6.5; 60 -6.9; 66 -7.1; 72 -7.3; 79 -7.4; 87 -7.4; 96 -7.4; 106 -7.4; 116 -7.4; 128 -7.4; 141 -7.2; 155 -7.0; 170 -6.7; 187 -6.4; 206 -6.1; 227 -5.7; 249 -5.2; 274 -4.7; 302 -4.2; 332 -3.8; 365 -3.4; 402 -3.2; 442 -3.2; 486 -3.2; 535 -3.6; 588 -4.4; 647 -5.4; 712 -6.4; 783 -7.2; 861 -8.0; 947 -8.6; 1042 -9.1; 1146 -9.3; 1261 -9.6; 1387 -9.9; 1526 -9.1; 1678 -8.2; 1846 -9.6; 2031 -11.5; 2234 -11.9; 2457 -10.9; 2703 -8.8; 2973 -6.3; 3270 -3.1; 3597 -0.5; 3957 -3.1; 4353 -7.4; 4788 -8.9; 5267 -7.5; 5793 -4.5; 6373 -3.4; 7010 -5.5; 7711 -7.5; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`German Maestro GMP 450 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `German Maestro GMP 450 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 2.03 | 6.0 dB  |
| Peaking | 445 Hz  | 1.35 | 4.1 dB  |
| Peaking | 1140 Hz | 1.3  | -3.3 dB |
| Peaking | 2250 Hz | 2.98 | -5.4 dB |
| Peaking | 3554 Hz | 5.48 | 7.4 dB  |
| Peaking | 34 Hz   | 2.01 | 0.8 dB  |
| Peaking | 95 Hz   | 1.08 | -1.3 dB |
| Peaking | 4861 Hz | 5.08 | -3.9 dB |
| Peaking | 6292 Hz | 3.07 | 4.0 dB  |
| Peaking | 7678 Hz | 4.17 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/German%20Maestro%20GMP%20450%20PRO/German%20Maestro%20GMP%20450%20PRO.png)