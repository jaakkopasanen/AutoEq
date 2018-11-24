# Zipbuds Pro Mic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.5dB
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.7; 28 -8.1; 31 -8.3; 34 -8.5; 37 -8.6; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.4; 60 -9.5; 66 -9.7; 72 -9.7; 79 -10.0; 87 -10.0; 96 -10.2; 106 -10.1; 116 -10.0; 128 -9.9; 141 -9.8; 155 -9.5; 170 -9.3; 187 -8.9; 206 -8.5; 227 -8.0; 249 -7.6; 274 -7.0; 302 -6.4; 332 -5.8; 365 -5.1; 402 -4.4; 442 -3.6; 486 -3.2; 535 -2.6; 588 -1.6; 647 -1.1; 712 -0.6; 783 -0.0; 861 0.2; 947 0.2; 1042 0.0; 1146 0.4; 1261 0.1; 1387 -0.6; 1526 -1.6; 1678 -2.5; 1846 -3.0; 2031 -3.3; 2234 -3.5; 2457 -3.5; 2703 -3.9; 2973 -3.3; 3270 -2.3; 3597 -1.5; 3957 -3.0; 4353 -7.1; 4788 -11.9; 5267 -11.3; 5793 -5.3; 6373 -2.3; 7010 -3.2; 7711 -7.7; 8482 -10.2; 9330 -5.7; 10263 -1.3; 11289 -1.8; 12418 -1.5; 13660 -0.6; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zipbuds Pro Mic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zipbuds Pro Mic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.32 | -8.2 dB  |
| Peaking | 144 Hz   | 0.74 | -5.1 dB  |
| Peaking | 295 Hz   | 1.32 | -3.0 dB  |
| Peaking | 5578 Hz  | 0.75 | -7.5 dB  |
| Peaking | 24000 Hz | 2.51 | -6.5 dB  |
| Peaking | 2293 Hz  | 2.09 | -2.7 dB  |
| Peaking | 3729 Hz  | 4.6  | 3.4 dB   |
| Peaking | 5031 Hz  | 2.86 | -14.1 dB |
| Peaking | 6253 Hz  | 1.07 | 12.1 dB  |
| Peaking | 8300 Hz  | 3.23 | -12.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zipbuds%20Pro%20Mic/Zipbuds%20Pro%20Mic.png)