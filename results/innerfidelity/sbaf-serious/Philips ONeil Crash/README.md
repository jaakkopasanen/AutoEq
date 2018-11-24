# Philips ONeil Crash

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -8.2; 23 -8.5; 25 -8.8; 28 -9.1; 31 -9.4; 34 -9.6; 37 -9.8; 41 -10.0; 45 -10.1; 49 -10.2; 54 -10.3; 60 -10.4; 66 -10.7; 72 -10.9; 79 -11.1; 87 -11.5; 96 -11.6; 106 -11.6; 116 -11.6; 128 -12.2; 141 -12.5; 155 -12.1; 170 -11.2; 187 -11.4; 206 -10.8; 227 -10.1; 249 -9.3; 274 -8.3; 302 -7.4; 332 -6.7; 365 -6.1; 402 -5.9; 442 -5.3; 486 -5.0; 535 -4.5; 588 -3.6; 647 -2.7; 712 -1.8; 783 -1.2; 861 -0.7; 947 -0.1; 1042 0.1; 1146 -0.1; 1261 -0.2; 1387 -1.1; 1526 -2.0; 1678 -2.5; 1846 -3.4; 2031 -4.5; 2234 -6.1; 2457 -7.2; 2703 -7.4; 2973 -6.4; 3270 -4.7; 3597 -1.6; 3957 0.8; 4353 -1.5; 4788 2.1; 5267 4.8; 5793 3.7; 6373 0.3; 7010 -2.6; 7711 -4.8; 8482 -6.1; 9330 -5.2; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.4; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips ONeil Crash GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips ONeil Crash ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.24 | -8.4 dB |
| Peaking | 180 Hz  | 0.53 | -7.9 dB |
| Peaking | 2553 Hz | 2.6  | -8.1 dB |
| Peaking | 8599 Hz | 4.47 | -7.0 dB |
| Peaking | 1036 Hz | 2.74 | 1.7 dB  |
| Peaking | 1838 Hz | 3.98 | -1.3 dB |
| Peaking | 3140 Hz | 8.02 | -2.2 dB |
| Peaking | 5421 Hz | 3.93 | 6.1 dB  |
| Peaking | 7315 Hz | 5.48 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20ONeil%20Crash/Philips%20ONeil%20Crash.png)