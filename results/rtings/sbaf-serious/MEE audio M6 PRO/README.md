# MEE audio M6 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.7; 28 1.3; 31 1.0; 34 0.8; 37 0.6; 41 0.4; 45 0.3; 49 0.1; 54 -0.1; 60 -0.4; 66 -0.7; 72 -0.8; 79 -1.0; 87 -1.3; 96 -1.6; 106 -2.1; 116 -2.5; 128 -2.9; 141 -3.2; 155 -3.3; 170 -3.3; 187 -3.3; 206 -3.2; 227 -3.1; 249 -2.8; 274 -2.2; 302 -1.7; 332 -1.0; 365 -0.4; 402 0.1; 442 0.4; 486 0.9; 535 1.5; 588 1.9; 647 2.1; 712 2.2; 783 1.9; 861 1.2; 947 0.4; 1042 -0.3; 1146 -1.2; 1261 -1.6; 1387 -2.4; 1526 -3.3; 1678 -4.1; 1846 -4.5; 2031 -5.1; 2234 -5.6; 2457 -6.4; 2703 -7.7; 2973 -7.4; 3270 -5.6; 3597 -4.5; 3957 -5.9; 4353 -9.4; 4788 -12.3; 5267 -12.3; 5793 -4.7; 6373 -1.0; 7010 0.4; 7711 -1.9; 8482 -4.5; 9330 -2.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MEE audio M6 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MEE audio M6 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.31 | 2.3 dB   |
| Peaking | 162 Hz   | 1.16 | -3.8 dB  |
| Peaking | 2567 Hz  | 1.41 | -6.8 dB  |
| Peaking | 4918 Hz  | 3.87 | -12.6 dB |
| Peaking | 23999 Hz | 2.28 | -1.5 dB  |
| Peaking | 262 Hz   | 2.97 | -1.2 dB  |
| Peaking | 672 Hz   | 1.46 | 2.9 dB   |
| Peaking | 1519 Hz  | 2.51 | -1.5 dB  |
| Peaking | 6794 Hz  | 5.27 | 3.2 dB   |
| Peaking | 8565 Hz  | 6.19 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/MEE%20audio%20M6%20PRO/MEE%20audio%20M6%20PRO.png)