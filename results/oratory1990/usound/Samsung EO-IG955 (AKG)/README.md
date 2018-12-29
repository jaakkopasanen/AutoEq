# Samsung EO-IG955 (AKG)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -3.8; 23 -4.1; 25 -4.4; 28 -4.7; 31 -5.0; 34 -5.2; 37 -5.4; 41 -5.7; 45 -5.9; 49 -6.0; 54 -6.2; 60 -6.5; 66 -6.7; 72 -6.9; 79 -7.1; 87 -7.3; 96 -7.5; 106 -7.6; 116 -7.7; 128 -7.7; 141 -7.6; 155 -7.4; 170 -7.0; 187 -6.3; 206 -6.5; 227 -6.3; 249 -5.9; 274 -5.4; 302 -4.8; 332 -4.4; 365 -3.8; 402 -3.3; 442 -2.8; 486 -2.3; 535 -1.8; 588 -1.3; 647 -0.9; 712 -0.4; 783 0.0; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.4; 1526 -1.6; 1678 -1.6; 1846 -1.6; 2031 -1.7; 2234 -2.1; 2457 -2.5; 2703 -2.9; 2973 -3.5; 3270 -4.0; 3597 -4.1; 3957 -3.6; 4353 -2.8; 4788 -3.2; 5267 -4.2; 5793 -2.7; 6373 -0.3; 7010 -1.3; 7711 -6.3; 8482 -8.2; 9330 -7.4; 10263 -7.6; 11289 -7.4; 12418 -7.2; 13660 -10.5; 15026 -14.1; 16529 -14.0; 18182 -10.1; 20000 -2.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung EO-IG955 (AKG) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung EO-IG955 (AKG) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.32 | -5.8 dB  |
| Peaking | 190 Hz   | 0.64 | -3.7 dB  |
| Peaking | 3295 Hz  | 1.31 | -3.6 dB  |
| Peaking | 8799 Hz  | 3.37 | -5.2 dB  |
| Peaking | 15939 Hz | 1    | -15.0 dB |
| Peaking | 862 Hz   | 2.54 | 1.3 dB   |
| Peaking | 1485 Hz  | 2.72 | -0.8 dB  |
| Peaking | 5394 Hz  | 5.84 | -2.4 dB  |
| Peaking | 6664 Hz  | 4.16 | 3.8 dB   |
| Peaking | 7832 Hz  | 7.05 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Samsung%20EO-IG955%20(AKG)/Samsung%20EO-IG955%20(AKG).png)