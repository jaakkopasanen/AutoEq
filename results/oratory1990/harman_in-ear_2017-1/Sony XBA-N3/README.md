# Sony XBA-N3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.5; 28 -4.7; 31 -4.8; 34 -4.8; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.9; 54 -4.9; 60 -4.8; 66 -4.8; 72 -4.8; 79 -4.8; 87 -4.7; 96 -4.5; 106 -4.2; 116 -4.5; 128 -4.9; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.0; 206 -3.7; 227 -3.2; 249 -2.9; 274 -2.5; 302 -2.0; 332 -1.5; 365 -1.1; 402 -0.7; 442 -0.5; 486 -0.2; 535 0.1; 588 0.3; 647 0.5; 712 0.6; 783 0.7; 861 0.6; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.0; 1387 -0.8; 1526 0.4; 1678 1.1; 1846 1.0; 2031 1.3; 2234 2.2; 2457 3.4; 2703 4.6; 2973 5.5; 3270 5.6; 3597 3.9; 3957 2.6; 4353 4.0; 4788 3.0; 5267 3.5; 5793 4.9; 6373 4.7; 7010 2.2; 7711 0.3; 8482 -0.7; 9330 -2.1; 10263 -2.6; 11289 -1.8; 12418 -2.0; 13660 -8.1; 15026 -18.3; 16529 -22.5; 18182 -17.0; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.33 | -4.8 dB  |
| Peaking | 166 Hz   | 1.01 | -2.9 dB  |
| Peaking | 3016 Hz  | 3.1  | 3.9 dB   |
| Peaking | 9286 Hz  | 0.38 | 7.5 dB   |
| Peaking | 16448 Hz | 1.05 | -28.6 dB |
| Peaking | 1287 Hz  | 4.84 | -1.8 dB  |
| Peaking | 6108 Hz  | 4.2  | 3.4 dB   |
| Peaking | 9424 Hz  | 1.33 | -3.3 dB  |
| Peaking | 12436 Hz | 2.53 | 5.7 dB   |
| Peaking | 14935 Hz | 5.07 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-N3/Sony%20XBA-N3.png)