# Sony MH1C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.9; 23 -10.7; 25 -10.6; 28 -10.4; 31 -10.2; 34 -10.0; 37 -9.8; 41 -9.5; 45 -9.2; 49 -9.0; 54 -8.8; 60 -8.5; 66 -8.3; 72 -8.2; 79 -8.0; 87 -7.8; 96 -7.7; 106 -7.4; 116 -7.1; 128 -6.9; 141 -6.5; 155 -6.2; 170 -5.8; 187 -5.4; 206 -4.9; 227 -4.4; 249 -4.0; 274 -3.5; 302 -3.0; 332 -2.5; 365 -2.0; 402 -1.6; 442 -1.0; 486 -0.8; 535 -0.4; 588 0.2; 647 0.4; 712 0.4; 783 0.6; 861 0.4; 947 -0.0; 1042 -0.1; 1146 -1.1; 1261 -1.2; 1387 -1.5; 1526 -2.1; 1678 -2.7; 1846 -2.9; 2031 -2.8; 2234 -2.7; 2457 -2.1; 2703 -1.6; 2973 -0.4; 3270 1.4; 3597 2.8; 3957 3.1; 4353 2.4; 4788 3.2; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.5; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH1C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH1C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.18 | -10.6 dB |
| Peaking | 156 Hz   | 0.8  | -3.1 dB  |
| Peaking | 2073 Hz  | 1.58 | -3.4 dB  |
| Peaking | 3718 Hz  | 3.25 | 3.2 dB   |
| Peaking | 5788 Hz  | 3.07 | 6.6 dB   |
| Peaking | 308 Hz   | 1.88 | -0.6 dB  |
| Peaking | 782 Hz   | 1.14 | 1.5 dB   |
| Peaking | 1271 Hz  | 1.72 | -0.9 dB  |
| Peaking | 15158 Hz | 3.45 | -0.1 dB  |
| Peaking | 15249 Hz | 5.06 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MH1C/Sony%20MH1C.png)