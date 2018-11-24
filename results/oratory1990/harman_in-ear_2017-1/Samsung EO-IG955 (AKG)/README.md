# Samsung EO-IG955 (AKG)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.7; 28 -5.0; 31 -5.3; 34 -5.6; 37 -5.8; 41 -6.0; 45 -6.2; 49 -6.4; 54 -6.6; 60 -6.8; 66 -7.0; 72 -7.2; 79 -7.4; 87 -7.6; 96 -7.8; 106 -7.9; 116 -8.0; 128 -8.0; 141 -7.9; 155 -7.7; 170 -7.4; 187 -6.6; 206 -6.8; 227 -6.7; 249 -6.2; 274 -5.7; 302 -5.1; 332 -4.5; 365 -3.9; 402 -3.4; 442 -2.8; 486 -2.2; 535 -1.7; 588 -1.2; 647 -0.7; 712 -0.2; 783 0.2; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -0.7; 1526 -0.7; 1678 -0.6; 1846 -0.6; 2031 -0.4; 2234 -0.1; 2457 0.0; 2703 0.0; 2973 -0.4; 3270 -1.0; 3597 -1.3; 3957 -1.2; 4353 -0.8; 4788 -1.5; 5267 -2.5; 5793 -0.7; 6373 2.1; 7010 1.9; 7711 -2.5; 8482 -5.6; 9330 -7.5; 10263 -9.1; 11289 -7.9; 12418 -8.9; 13660 -18.6; 15026 -29.6; 16529 -32.0; 18182 -25.7; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung EO-IG955 (AKG) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung EO-IG955 (AKG) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.36 | -5.3 dB  |
| Peaking | 132 Hz   | 0.76 | -4.5 dB  |
| Peaking | 275 Hz   | 1.2  | -3.1 dB  |
| Peaking | 15580 Hz | 2.04 | -22.0 dB |
| Peaking | 17808 Hz | 1.17 | -21.0 dB |
| Peaking | 823 Hz   | 4.24 | 1.1 dB   |
| Peaking | 5355 Hz  | 4.29 | -2.1 dB  |
| Peaking | 6693 Hz  | 3.8  | 6.0 dB   |
| Peaking | 9147 Hz  | 3.81 | -3.2 dB  |
| Peaking | 24000 Hz | 1.76 | 0.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Samsung%20EO-IG955%20(AKG)/Samsung%20EO-IG955%20(AKG).png)