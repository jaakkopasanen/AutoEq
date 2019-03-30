# NuForce Primo 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.5; 25 -11.4; 28 -11.2; 31 -11.1; 34 -11.0; 37 -10.9; 41 -10.8; 45 -10.7; 49 -10.8; 54 -10.8; 60 -10.6; 66 -10.4; 72 -10.4; 79 -10.4; 87 -10.4; 96 -10.2; 106 -10.1; 116 -10.1; 128 -10.1; 141 -10.1; 155 -10.1; 170 -10.1; 187 -10.1; 206 -9.8; 227 -9.8; 249 -9.7; 274 -9.5; 302 -9.5; 332 -9.3; 365 -9.1; 402 -9.1; 442 -8.9; 486 -8.8; 535 -8.5; 588 -8.5; 647 -8.5; 712 -8.3; 783 -8.2; 861 -8.2; 947 -8.2; 1042 -8.4; 1146 -8.6; 1261 -8.9; 1387 -9.3; 1526 -10.0; 1678 -10.6; 1846 -10.8; 2031 -10.4; 2234 -9.2; 2457 -7.8; 2703 -6.6; 2973 -5.8; 3270 -5.1; 3597 -4.0; 3957 -3.0; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Primo 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Primo 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.83 | -4.1 dB |
| Peaking | 28 Hz   | 0.37 | -3.0 dB |
| Peaking | 197 Hz  | 0.29 | -2.9 dB |
| Peaking | 1809 Hz | 1.78 | -4.5 dB |
| Peaking | 5037 Hz | 1.68 | 6.8 dB  |
| Peaking | 3271 Hz | 2.82 | 0.5 dB  |
| Peaking | 5080 Hz | 6.23 | -0.7 dB |
| Peaking | 6474 Hz | 3.16 | 3.2 dB  |
| Peaking | 7455 Hz | 1.84 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/NuForce%20Primo%208/NuForce%20Primo%208.png)