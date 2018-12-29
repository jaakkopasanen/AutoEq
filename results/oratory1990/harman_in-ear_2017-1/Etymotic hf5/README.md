# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.8; 45 5.6; 49 5.4; 54 5.2; 60 4.9; 66 4.5; 72 4.2; 79 3.8; 87 3.2; 96 2.9; 106 2.1; 116 2.1; 128 1.6; 141 1.0; 155 0.8; 170 0.6; 187 0.4; 206 0.2; 227 0.1; 249 0.0; 274 -0.0; 302 -0.0; 332 0.1; 365 0.2; 402 0.2; 442 0.2; 486 0.2; 535 0.3; 588 0.5; 647 0.6; 712 0.7; 783 0.8; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.1; 1387 -1.0; 1526 -0.7; 1678 -0.3; 1846 0.2; 2031 0.9; 2234 1.7; 2457 2.3; 2703 2.7; 2973 3.1; 3270 3.5; 3597 3.7; 3957 4.0; 4353 4.5; 4788 5.4; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -5.2; 15026 -15.9; 16529 -13.4; 18182 -2.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.19 | 6.2 dB   |
| Peaking | 150 Hz   | 0.74 | -2.5 dB  |
| Peaking | 1380 Hz  | 3.09 | -1.8 dB  |
| Peaking | 4936 Hz  | 0.97 | 5.9 dB   |
| Peaking | 15636 Hz | 2.87 | -18.9 dB |
| Peaking | 4368 Hz  | 4.1  | -1.6 dB  |
| Peaking | 6575 Hz  | 1.65 | 3.3 dB   |
| Peaking | 7696 Hz  | 2.5  | -4.6 dB  |
| Peaking | 13000 Hz | 3.43 | 4.5 dB   |
| Peaking | 14451 Hz | 5.68 | -5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Etymotic%20hf5/Etymotic%20hf5.png)