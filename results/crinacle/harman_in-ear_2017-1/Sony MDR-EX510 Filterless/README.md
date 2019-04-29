# Sony MDR-EX510 Filterless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.1; 34 -2.5; 37 -2.8; 41 -3.1; 45 -3.3; 49 -3.6; 54 -3.9; 60 -4.2; 66 -4.6; 72 -4.9; 79 -5.3; 87 -5.7; 96 -6.2; 106 -6.5; 116 -6.9; 128 -7.3; 141 -7.5; 155 -7.7; 170 -7.8; 187 -7.9; 206 -7.9; 227 -7.8; 249 -7.7; 274 -7.6; 302 -7.3; 332 -6.9; 365 -6.5; 402 -6.3; 442 -6.0; 486 -5.6; 535 -5.3; 588 -4.8; 647 -4.3; 712 -3.8; 783 -3.3; 861 -3.0; 947 -2.8; 1042 -3.0; 1146 -3.4; 1261 -3.8; 1387 -3.9; 1526 -3.8; 1678 -3.7; 1846 -3.7; 2031 -3.9; 2234 -4.0; 2457 -3.8; 2703 -3.6; 2973 -3.2; 3270 -2.1; 3597 -1.6; 3957 -1.7; 4353 -2.7; 4788 -4.9; 5267 -7.7; 5793 -6.5; 6373 -2.6; 7010 -2.3; 7711 -4.5; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -12.3; 15026 -17.3; 16529 -18.1; 18182 -17.6; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX510 Filterless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX510 Filterless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.44 | 5.1 dB   |
| Peaking | 186 Hz   | 0.72 | -3.5 dB  |
| Peaking | 5391 Hz  | 5.83 | -6.0 dB  |
| Peaking | 11867 Hz | 0.24 | 20.1 dB  |
| Peaking | 15966 Hz | 0.32 | -31.0 dB |
| Peaking | 893 Hz   | 2.5  | 1.7 dB   |
| Peaking | 2466 Hz  | 1.12 | -1.2 dB  |
| Peaking | 3640 Hz  | 3.29 | 2.0 dB   |
| Peaking | 8596 Hz  | 4.2  | -1.8 dB  |
| Peaking | 12316 Hz | 7.37 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.3 dB   |
| Peaking | 125 Hz   | 1.41 | -2.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -16.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20MDR-EX510%20Filterless/Sony%20MDR-EX510%20Filterless.png)