# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -8.8; 23 -9.1; 25 -9.3; 28 -9.5; 31 -9.6; 34 -9.6; 37 -9.5; 41 -9.5; 45 -9.5; 49 -9.5; 54 -9.6; 60 -9.8; 66 -10.0; 72 -10.2; 79 -10.4; 87 -10.7; 96 -10.9; 106 -11.2; 116 -11.3; 128 -11.4; 141 -11.4; 155 -11.3; 170 -11.2; 187 -10.9; 206 -10.5; 227 -10.0; 249 -9.4; 274 -9.9; 302 -9.1; 332 -8.3; 365 -7.5; 402 -6.8; 442 -6.1; 486 -5.3; 535 -4.5; 588 -3.6; 647 -2.8; 712 -2.0; 783 -1.2; 861 -0.5; 947 -0.1; 1042 0.1; 1146 0.3; 1261 0.6; 1387 0.9; 1526 1.3; 1678 1.6; 1846 1.9; 2031 2.2; 2234 2.8; 2457 3.4; 2703 4.0; 2973 4.5; 3270 4.9; 3597 5.0; 3957 4.8; 4353 4.2; 4788 3.2; 5267 1.7; 5793 -1.0; 6373 -5.2; 7010 -7.6; 7711 -6.6; 8482 -4.8; 9330 -6.1; 10263 -7.8; 11289 -7.0; 12418 -8.7; 13660 -14.3; 15026 -19.1; 16529 -20.4; 18182 -15.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 38 Hz    | 0.15 | -9.1 dB  |
| Peaking | 222 Hz   | 0.57 | -5.7 dB  |
| Peaking | 3376 Hz  | 1.05 | 6.8 dB   |
| Peaking | 16384 Hz | 0.6  | -21.0 dB |
| Peaking | 22050 Hz | 1.14 | -6.3 dB  |
| Peaking | 1000 Hz  | 2.12 | 1.1 dB   |
| Peaking | 4998 Hz  | 3.44 | 2.2 dB   |
| Peaking | 6850 Hz  | 4.23 | -5.5 dB  |
| Peaking | 11969 Hz | 3.18 | 3.7 dB   |
| Peaking | 14407 Hz | 3.61 | -1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)