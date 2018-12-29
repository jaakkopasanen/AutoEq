# AKG Q350 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 21 -7.4; 23 -7.8; 25 -8.2; 28 -8.6; 31 -9.0; 34 -9.3; 37 -9.5; 41 -9.7; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.7; 66 -11.0; 72 -11.1; 79 -11.3; 87 -11.4; 96 -11.4; 106 -11.4; 116 -11.3; 128 -11.3; 141 -11.1; 155 -10.9; 170 -10.6; 187 -10.2; 206 -9.7; 227 -9.2; 249 -8.7; 274 -8.1; 302 -7.4; 332 -6.6; 365 -5.8; 402 -5.1; 442 -4.4; 486 -3.7; 535 -3.0; 588 -2.2; 647 -1.5; 712 -0.9; 783 -0.4; 861 -0.1; 947 0.2; 1042 0.0; 1146 0.0; 1261 -0.0; 1387 -0.3; 1526 -0.6; 1678 -0.7; 1846 -0.5; 2031 -0.1; 2234 0.3; 2457 0.5; 2703 0.6; 2973 0.2; 3270 -0.8; 3597 -3.0; 3957 -4.4; 4353 -5.7; 4788 -7.5; 5267 -9.9; 5793 -13.1; 6373 -8.4; 7010 -5.1; 7711 -4.8; 8482 -8.2; 9330 -10.0; 10263 -3.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.9; 16529 -1.4; 18182 0.0; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q350 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q350 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.33 | -9.1 dB  |
| Peaking | 144 Hz   | 0.72 | -5.7 dB  |
| Peaking | 296 Hz   | 1.23 | -3.5 dB  |
| Peaking | 5925 Hz  | 1.48 | -11.0 dB |
| Peaking | 21556 Hz | 1.91 | -6.9 dB  |
| Peaking | 2779 Hz  | 1.93 | 2.8 dB   |
| Peaking | 7251 Hz  | 3.35 | 7.5 dB   |
| Peaking | 9437 Hz  | 1.52 | -19.8 dB |
| Peaking | 10560 Hz | 1.32 | 14.4 dB  |
| Peaking | 15518 Hz | 5.99 | -3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20Q350%20Quincy%20Jones/AKG%20Q350%20Quincy%20Jones.png)