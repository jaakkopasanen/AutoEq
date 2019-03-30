# Sony MDR-10RC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.4; 79 -2.3; 87 -2.9; 96 -3.4; 106 -3.7; 116 -3.7; 128 -3.9; 141 -4.1; 155 -4.0; 170 -4.0; 187 -4.0; 206 -4.1; 227 -4.3; 249 -4.4; 274 -4.6; 302 -4.7; 332 -5.0; 365 -5.1; 402 -5.8; 442 -6.4; 486 -6.7; 535 -6.6; 588 -6.6; 647 -6.6; 712 -6.8; 783 -6.7; 861 -6.5; 947 -6.1; 1042 -6.0; 1146 -6.0; 1261 -5.9; 1387 -6.1; 1526 -6.6; 1678 -7.1; 1846 -7.7; 2031 -8.7; 2234 -9.2; 2457 -9.0; 2703 -7.7; 2973 -5.3; 3270 -2.2; 3597 -0.5; 3957 -2.6; 4353 -8.7; 4788 -12.7; 5267 -13.7; 5793 -12.3; 6373 -11.2; 7010 -11.2; 7711 -10.6; 8482 -9.1; 9330 -7.9; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -6.9; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-10RC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-10RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.41 | 6.4 dB   |
| Peaking | 236 Hz   | 1.42 | 1.5 dB   |
| Peaking | 2408 Hz  | 2.59 | -4.1 dB  |
| Peaking | 3696 Hz  | 2.07 | 13.8 dB  |
| Peaking | 4912 Hz  | 1.34 | -12.0 dB |
| Peaking | 100 Hz   | 5.5  | -0.5 dB  |
| Peaking | 599 Hz   | 1.96 | -0.6 dB  |
| Peaking | 1188 Hz  | 2.71 | 0.9 dB   |
| Peaking | 7654 Hz  | 5.69 | -1.5 dB  |
| Peaking | 11509 Hz | 1.63 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 1.3 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-10RC/Sony%20MDR-10RC.png)