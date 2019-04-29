# Earsonics ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -11.8; 25 -11.9; 28 -12.0; 31 -12.1; 34 -12.1; 37 -12.1; 41 -12.1; 45 -12.1; 49 -12.1; 54 -12.0; 60 -12.0; 66 -11.9; 72 -11.9; 79 -11.9; 87 -11.8; 96 -11.7; 106 -11.4; 116 -11.0; 128 -10.7; 141 -10.2; 155 -9.6; 170 -9.0; 187 -8.5; 206 -8.1; 227 -7.7; 249 -7.5; 274 -7.5; 302 -7.6; 332 -7.7; 365 -7.8; 402 -8.0; 442 -8.2; 486 -8.4; 535 -8.5; 588 -8.5; 647 -8.5; 712 -8.4; 783 -8.3; 861 -8.3; 947 -8.6; 1042 -9.1; 1146 -9.9; 1261 -10.4; 1387 -10.4; 1526 -9.7; 1678 -8.8; 1846 -7.1; 2031 -3.8; 2234 -1.4; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -2.9; 3957 -2.9; 4353 -0.6; 4788 -0.5; 5267 -1.9; 5793 -2.5; 6373 -6.0; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -14.6; 15026 -22.6; 16529 -22.8; 18182 -12.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.32 | -6.0 dB  |
| Peaking | 1652 Hz  | 0.83 | -7.2 dB  |
| Peaking | 2355 Hz  | 1.65 | 8.8 dB   |
| Peaking | 4390 Hz  | 0.77 | 5.1 dB   |
| Peaking | 15926 Hz | 1.87 | -20.0 dB |
| Peaking | 3826 Hz  | 6.13 | -3.3 dB  |
| Peaking | 4693 Hz  | 1.58 | 2.3 dB   |
| Peaking | 6534 Hz  | 2.37 | -2.5 dB  |
| Peaking | 12134 Hz | 2.81 | 4.3 dB   |
| Peaking | 14282 Hz | 3.81 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB   |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -17.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Earsonics%20ES3/Earsonics%20ES3.png)