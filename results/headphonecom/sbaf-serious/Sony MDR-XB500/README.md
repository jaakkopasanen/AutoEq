# Sony MDR-XB500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -9.2; 23 -9.4; 25 -9.5; 28 -9.7; 31 -9.8; 34 -9.9; 37 -10.0; 41 -10.0; 45 -10.1; 49 -10.2; 54 -10.3; 60 -10.3; 66 -10.2; 72 -10.3; 79 -10.9; 87 -11.5; 96 -11.7; 106 -11.4; 116 -12.0; 128 -12.6; 141 -13.2; 155 -13.4; 170 -12.5; 187 -12.4; 206 -13.3; 227 -13.6; 249 -13.1; 274 -12.7; 302 -12.4; 332 -12.0; 365 -11.5; 402 -10.8; 442 -10.0; 486 -9.0; 535 -7.6; 588 -6.0; 647 -4.1; 712 -2.0; 783 -0.1; 861 1.1; 947 0.7; 1042 -0.4; 1146 -1.6; 1261 -3.2; 1387 -4.6; 1526 -5.2; 1678 -4.8; 1846 -3.8; 2031 -2.6; 2234 -1.2; 2457 0.6; 2703 2.6; 2973 4.2; 3270 6.0; 3597 6.0; 3957 4.5; 4353 0.7; 4788 -2.4; 5267 -1.6; 5793 0.1; 6373 0.8; 7010 -1.5; 7711 -1.5; 8482 0.0; 9330 -0.0; 10263 -1.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-XB500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.18 | -9.2 dB |
| Peaking | 225 Hz   | 0.65 | -8.1 dB |
| Peaking | 414 Hz   | 1.93 | -4.1 dB |
| Peaking | 3414 Hz  | 4.25 | 7.4 dB  |
| Peaking | 914 Hz   | 1.79 | 7.2 dB  |
| Peaking | 1762 Hz  | 0.69 | -9.1 dB |
| Peaking | 2610 Hz  | 1.06 | 7.2 dB  |
| Peaking | 4872 Hz  | 7.27 | -3.4 dB |
| Peaking | 22309 Hz | 1.69 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)