# Ultimate Ears UE18+ 3rd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.2; 28 -4.6; 31 -5.0; 34 -5.3; 37 -5.5; 41 -5.8; 45 -6.1; 49 -6.3; 54 -6.7; 60 -7.1; 66 -7.5; 72 -7.9; 79 -8.3; 87 -8.8; 96 -9.3; 106 -9.7; 116 -10.1; 128 -10.5; 141 -10.9; 155 -11.2; 170 -11.4; 187 -11.6; 206 -11.7; 227 -11.9; 249 -11.9; 274 -12.0; 302 -12.0; 332 -11.8; 365 -11.8; 402 -11.8; 442 -11.9; 486 -11.8; 535 -11.8; 588 -11.8; 647 -11.5; 712 -11.1; 783 -10.3; 861 -9.2; 947 -8.1; 1042 -7.2; 1146 -6.8; 1261 -6.7; 1387 -6.6; 1526 -6.3; 1678 -5.5; 1846 -4.1; 2031 -2.5; 2234 -1.3; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.6; 5793 -1.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.3; 15026 -26.7; 16529 -36.8; 18182 -31.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE18+ 3rd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE18+ 3rd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.28 | 3.5 dB   |
| Peaking | 408 Hz   | 0.24 | -6.3 dB  |
| Peaking | 4567 Hz  | 0.35 | 11.1 dB  |
| Peaking | 12616 Hz | 2.04 | 13.3 dB  |
| Peaking | 16611 Hz | 0.84 | -36.6 dB |
| Peaking | 1094 Hz  | 2.3  | 2.6 dB   |
| Peaking | 1634 Hz  | 0.77 | -2.6 dB  |
| Peaking | 2258 Hz  | 2.03 | 2.9 dB   |
| Peaking | 10230 Hz | 5.14 | 1.5 dB   |
| Peaking | 17795 Hz | 4.76 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | -0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 16000 Hz | 1.41 | -29.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE18+%203rd%20Gen/Ultimate%20Ears%20UE18+%203rd%20Gen.png)